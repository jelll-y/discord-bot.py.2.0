import discord
import asyncio
from discord.ext import commands
import os


class Admin(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Admin command is loaded')

    @commands.command()
    @commands.is_owner()
    async def sync(self, ctx) -> None:
        fmt = await ctx.bot.tree.sync()
        await ctx.send(f'Re-Synced {len(fmt)} commands to all servers.')
        return

    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, cog: str):
        try:
            await self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send("Could not unload cog")
            return
        await ctx.send("Cog unloaded")

    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, cog: str):
        try:
            await self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send("Could not load cog")
            return
        await ctx.send("Cog loaded")

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, cog: str):
        try:
            await self.bot.load_extension(cog)
            await self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send("Could not reload cog")
            return
        await ctx.send("Cog reloaded")


async def setup(bot):
    await bot.add_cog(Admin(bot))
