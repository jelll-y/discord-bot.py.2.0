import discord
from discord import app_commands
from discord.ext import commands
import os
import random as r


class Brendan(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Brendan command is loaded')

    @commands.hybrid_command(name="bgay")
    async def bgay(self, ctx: commands.Context):
        """Random image of the gay boy."""
        gay_boy = os.path.abspath('./images/brendan/image' + str(r.randint(0, 8)) + '.png')
        await ctx.send(file=discord.File(gay_boy))


async def setup(bot):
    await bot.add_cog(Brendan(bot))
