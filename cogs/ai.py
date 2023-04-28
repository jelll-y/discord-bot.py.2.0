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
        print('AI commands are loaded')

    @commands.command()
    async def ai(self, ctx: commands.Context, *, prompt: str):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"{prompt}",
            max_tokens=500,
            temperature=0.5)
        await ctx.reply(response.choices[0].text)

    @commands.command()
    async def image(self, ctx: commands.Context, *, prompt: str):
        response = openai.Image.create(
            prompt=f"{prompt}",
            n=1,
            size="512x512")
        await ctx.reply(response.data[0].url)


async def setup(bot):
    await bot.add_cog(ai(bot))
