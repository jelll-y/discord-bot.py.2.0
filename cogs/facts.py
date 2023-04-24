import discord
from discord.ext import commands
from discord import app_commands
import requests


class Facts(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Facts command is loaded')

    @commands.command()
    async def facts(self, ctx, number):
        response = requests.get(f'http://numbersapi.com/{number}')
        embed = discord.Embed(description=response.text)
        await ctx.channel.send(embed=embed)

    @app_commands.command(
        name="facts",
        description="Provides random fact for a number you enter")
    async def facts(self, interaction: discord.Interaction, number: int) -> None:
        response = requests.get(f'http://numbersapi.com/{number}')
        await interaction.response.send_message(f'{response.text}')


async def setup(bot):
    await bot.add_cog(Facts(bot))
