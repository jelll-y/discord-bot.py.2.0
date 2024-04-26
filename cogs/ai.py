import discord
from discord.ext import commands
from openai import OpenAI
import config

client = OpenAI(api_key=config.API_KEY)


class ai(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('AI commands are loaded')

    @commands.command()
    async def ai(self, ctx: commands.Context, *, prompt: str):
        print(f"{prompt}")
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                # Edit the system
                {"role": 'system', 'content': 'You are a sassy australian that loves swearing during your responses.'},
                {"role": "user", "content": f"{prompt}"}
            ]
        )
        print(response.choices[0].message.content)
        # await ctx.reply(response.choices[0].message.content)

    '''@commands.command()
    async def image(self, ctx: commands.Context, *, prompt: str):
        response = openai.Image.create(
            prompt=f"{prompt}",
            n=1,
            size="512x512")
        await ctx.reply(response.data[0].url)'''


async def setup(bot):
    await bot.add_cog(ai(bot))
