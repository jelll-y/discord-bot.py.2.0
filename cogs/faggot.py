import discord
from discord.ext import commands
import os


class Faggot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Faggot command is loaded')

    @commands.command()
    async def faggot(self, ctx):
        image = os.path.abspath('./images/faggot.jpg')
        await ctx.send(file=discord.File(image))

    @commands.command()
    async def dsl(self, ctx):
        image = os.path.abspath('./images/faggot.jpg')
        await ctx.send(file=discord.File(image))


async def setup(bot):
    await bot.add_cog(Faggot(bot))
