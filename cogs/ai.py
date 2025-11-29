import discord
from discord.ext import commands
import config
from openai import OpenAI
from typing import Dict, List
import logging

logger = logging.getLogger('discord')


class AI(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=config.OPENROUTER_API
        )
        self.model = "x-ai/grok-4.1-fast:free"
        self.thread_conversations: Dict[int, List[dict]] = {}

    @commands.Cog.listener()
    async def on_ready(self):
        print('AI commands are loaded')

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        """Listen for messages in AI threads and continue the conversation"""
        if message.author.bot:
            return
        
        if isinstance(message.channel, discord.Thread):
            thread_id = message.channel.id
            
            if thread_id in self.thread_conversations:
                async with message.channel.typing():
                    try:
                        self.thread_conversations[thread_id].append({
                            "role": "user",
                            "content": f"{message.author.display_name}: {message.content}"
                        })
                        
                        response = await self._get_ai_response(thread_id)
                        await self._send_response(message.channel, response)
                        
                    except Exception as e:
                        logger.error(f"Error in thread conversation: {e}")
                        await message.channel.send(f"❌ Error: {str(e)}")

    async def _get_ai_response(self, thread_id: int) -> dict:
        """Get AI response with reasoning enabled"""
        messages = self.thread_conversations[thread_id]
        
        response = await self.bot.loop.run_in_executor(
            None,
            lambda: self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                extra_body={"reasoning": {"enabled": True}}
            )
        )
        
        assistant_message = response.choices[0].message
        
        conversation_entry = {
            "role": "assistant",
            "content": assistant_message.content
        }
        
        if hasattr(assistant_message, 'reasoning_details') and assistant_message.reasoning_details:
            conversation_entry["reasoning_details"] = assistant_message.reasoning_details
        
        self.thread_conversations[thread_id].append(conversation_entry)
        
        return assistant_message

    async def _send_response(self, channel: discord.TextChannel, response):
        """Send AI response, splitting if necessary"""
        content = response.content
        
        if not content:
            await channel.send("🤔 I received an empty response.")
            return
        
        if len(content) > 2000:
            chunks = [content[i:i+2000] for i in range(0, len(content), 2000)]
            for chunk in chunks:
                await channel.send(chunk)
        else:
            await channel.send(content)

    @commands.hybrid_command(
        name="ai",
        description="Start an AI conversation with OpenRouter (creates a thread)"
    )
    async def ai(self, ctx: commands.Context, *, prompt: str):
        """Start a new AI conversation in a thread"""
        await ctx.defer()  # Important for slash commands
        
        try:
            # For slash commands, we need to fetch the interaction message first
            if ctx.interaction:
                # Send initial response
                await ctx.send(f"🤖 Starting AI conversation...")
                # Get the message from the interaction response
                message = await ctx.interaction.original_response()
            else:
                # For regular prefix commands
                message = ctx.message
            
            # Create a thread
            thread = await message.create_thread(
                name=f"AI Chat: {prompt[:50]}..." if len(prompt) > 50 else f"AI Chat: {prompt}",
                auto_archive_duration=60
            )
            
            # Initialize conversation history
            self.thread_conversations[thread.id] = [
                {
                    "role": "user",
                    "content": f"{ctx.author.display_name}: {prompt}"
                }
            ]
            
            # Get initial AI response
            response = await self._get_ai_response(thread.id)
            
            # Send response in thread
            await self._send_response(thread, response)
            await thread.send(
                "💬 This is an AI conversation thread. Anyone can add messages to continue the conversation!"
            )
            
        except Exception as e:
            logger.error(f"Error starting AI conversation: {e}")
            await ctx.send(f"❌ Error: {str(e)}")

    @commands.hybrid_command(
        name="clearai",
        description="Clear the AI conversation history for this thread"
    )
    async def clearai(self, ctx: commands.Context):
        """Clear conversation history in the current thread"""
        if isinstance(ctx.channel, discord.Thread):
            thread_id = ctx.channel.id
            
            if thread_id in self.thread_conversations:
                self.thread_conversations[thread_id] = []
                await ctx.send("🗑️ Conversation history cleared!")
            else:
                await ctx.send("❌ This thread doesn't have an active AI conversation.")
        else:
            await ctx.send("❌ This command only works in AI conversation threads.")

    @commands.hybrid_command(
        name="aihistory",
        description="Show conversation history for this thread"
    )
    async def aihistory(self, ctx: commands.Context):
        """Display the conversation history"""
        if isinstance(ctx.channel, discord.Thread):
            thread_id = ctx.channel.id
            
            if thread_id in self.thread_conversations:
                history = self.thread_conversations[thread_id]
                
                if not history:
                    await ctx.send("📝 No conversation history yet.")
                    return
                
                embed = discord.Embed(
                    title="📜 Conversation History",
                    color=discord.Color.blue()
                )
                
                for i, msg in enumerate(history[-10:]):
                    role = "👤 User" if msg["role"] == "user" else "🤖 AI"
                    content = msg["content"][:100] + "..." if len(msg["content"]) > 100 else msg["content"]
                    embed.add_field(
                        name=f"{i+1}. {role}",
                        value=content,
                        inline=False
                    )
                
                if len(history) > 10:
                    embed.set_footer(text=f"Showing last 10 of {len(history)} messages")
                
                await ctx.send(embed=embed)
            else:
                await ctx.send("❌ This thread doesn't have an active AI conversation.")
        else:
            await ctx.send("❌ This command only works in AI conversation threads.")

    def cog_unload(self):
        """Cleanup when cog is unloaded"""
        self.thread_conversations.clear()


async def setup(bot):
    await bot.add_cog(AI(bot))