import discord
from discord.ext import commands


class Admin(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Admin cog loaded')

    @commands.command()
    @commands.is_owner()
    async def sync(self, ctx) -> None:
        """Sync slash commands globally"""
        try:
            synced = await ctx.bot.tree.sync()
            await ctx.send(f'✅ Synced {len(synced)} commands globally')
        except Exception as e:
            await ctx.send(f'❌ Failed to sync: {e}')

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, cog: str):
        """Reload a cog (unload then load)"""
        try:
            await self.bot.reload_extension(cog)  # Use reload_extension instead
            await ctx.send(f'✅ Reloaded {cog}')
        except Exception as e:
            await ctx.send(f'❌ Could not reload {cog}: {e}')

    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, cog: str):
        """Load a cog"""
        try:
            await self.bot.load_extension(cog)
            await ctx.send(f'✅ Loaded {cog}')
        except Exception as e:
            await ctx.send(f'❌ Could not load {cog}: {e}')

    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, cog: str):
        """Unload a cog"""
        try:
            await self.bot.unload_extension(cog)
            await ctx.send(f'✅ Unloaded {cog}')
        except Exception as e:
            await ctx.send(f'❌ Could not unload {cog}: {e}')


async def setup(bot):
    await bot.add_cog(Admin(bot))