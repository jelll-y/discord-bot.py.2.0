import discord
from discord.ext import commands
import openai
import config
openai.org = config.ORG_ID
openai.api_key = config.API_KEY


class ai(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('AI command is loaded')

    @commands.command()
    async def ai(self, ctx: commands.Context, *, prompt: str):
        print(prompt)
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"{prompt}",
            max_tokens=100,
            temperature=0.5)
        print(response)
        await ctx.reply(response.choices[0].text)


async def setup(bot):
    await bot.add_cog(ai(bot))
