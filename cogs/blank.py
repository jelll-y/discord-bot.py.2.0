import discord
from discord.ext import commands


class Blank(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Blank command is loaded')

    @commands.command()
    async def default(self, ctx):
        return


async def setup(bot):
    await bot.add_cog(Blank(bot))
