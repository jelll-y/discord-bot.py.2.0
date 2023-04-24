import discord
from discord.ext import commands
from discord import app_commands
import os


class Faggot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Faggot command is loaded')

    @commands.hybrid_command(name="faggot")
    async def faggot(self, ctx: commands.Context):
        image = os.path.abspath('./images/faggot.jpg')
        await ctx.send(file=discord.File(image))

    @commands.hybrid_command(name="dsl")
    async def dsl(self, ctx: commands.Context):
        image = os.path.abspath('./images/faggot.jpg')
        await ctx.send(file=discord.File(image))


async def setup(bot):
    await bot.add_cog(Faggot(bot))
