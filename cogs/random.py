import discord
import random as r
from typing import Optional
from discord.ext import commands


class Random(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Random command is loaded')

    @commands.hybrid_command(
        name="random",
        description="Will choose a random option from your specified list."
    )
    async def random(self, ctx: commands.Context, *, option: str):
        if len(option) == 0:
            await ctx.send(f"Provide a few options {r.choice(self.bot.names)}.")
        else:
            options = ''.join(option)
            choice_list = options.split(', ')
            choice = r.choice(choice_list)
            if choice == 'kfc':
                await ctx.send('https://tenor.com/view/colonel-sanders-shirtless-abs-dancing-sparkles-gif-17679994')
            elif choice == 'maccas':
                await ctx.send('https://tenor.com/view/good-yes-mcdonalds-mcdo-thumbs-up-gif-16886848')
            else:
                await ctx.send(f'{choice}')

    @commands.command(
        name="r",
        description="Will choose a random option from your specified list."
    )
    async def r(self, ctx: commands.Context, *, option: str):
        if len(option) == 0:
            await ctx.send(f"Provide a few options {r.choice(self.bot.names)}.")
        else:
            options = ''.join(option)
            choice_list = options.split(', ')
            choice = r.choice(choice_list)
            if choice == 'kfc':
                await ctx.send('https://tenor.com/view/colonel-sanders-shirtless-abs-dancing-sparkles-gif-17679994')
            elif choice == 'maccas':
                await ctx.send('https://tenor.com/view/good-yes-mcdonalds-mcdo-thumbs-up-gif-16886848')
            else:
                await ctx.send(f'{choice}')

async def setup(bot):
    await bot.add_cog(Random(bot))
