import discord
from discord.ext import commands
import requests


class Facts(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Facts command is loaded')

    @commands.command()
    async def facts(self, ctx, number):
        response = requests.get(f'http://numbersapi.com/{number}')
        embed = discord.Embed(description=response.text)
        await ctx.channel.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Facts(bot))
