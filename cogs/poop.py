import discord
from discord.ext import commands
import random as r


class Poop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Poop command is loaded')

    @commands.command()
    async def poop(self, ctx):
        daniel = 194308223149277184
        toilets = list(['Main Shitter', 'Hardcore Gaming Shitter', 'Far Far Far away Shitter'])
        if ctx.author.id == daniel:
            await ctx.send(f'Go poop at the {r.choice(toilets)}')
        else:
            await ctx.send(f"Shit yourself {r.choice(self.bot.names)}.")


async def setup(bot):
    await bot.add_cog(Poop(bot))
