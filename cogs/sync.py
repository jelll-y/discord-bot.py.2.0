import discord
from discord.ext import commands
import os


class Sync(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Sync command is loaded')

    @commands.command()
    @commands.is_owner()
    async def sync(self, ctx) -> None:
        fmt = await ctx.bot.tree.sync()
        await ctx.send(f'Re-Synced {len(fmt)} commands to all servers.')
        return


async def setup(bot):
    await bot.add_cog(Sync(bot))
