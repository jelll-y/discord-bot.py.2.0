import datetime
import time
from typing import Optional

import discord
import requests
from discord.ext import commands

import random as r


def convert_to_unix_time_relative(days: int, hours: int, minutes: int, seconds: int) -> str:
    # Get the end date
    date = datetime.datetime.now()
    end_date = date + datetime.timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)

    # Get a tuple of the date attributes
    date_tuple = (end_date.year, end_date.month, end_date.day, end_date.hour, end_date.minute, end_date.second)

    # Convert to unix time
    return f'<t:{int(time.mktime(datetime.datetime(*date_tuple).timetuple()))}:R>'


def convert_to_unix_time(days: int, hours: int, minutes: int, seconds: int) -> str:
    # Get the end date
    date = datetime.datetime.now()
    end_date = date + datetime.timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)

    # Get a tuple of the date attributes
    date_tuple = (end_date.year, end_date.month, end_date.day, end_date.hour, end_date.minute, end_date.second)

    # Convert to unix time
    return f'<t:{int(time.mktime(datetime.datetime(*date_tuple).timetuple()))}>'


class Facts(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Facts command is loaded')

    @commands.hybrid_command(
        name="facts",
        description="Provides random fact for a number you enter")
    async def facts(self, interaction: discord.Interaction, number: int) -> None:
        response = requests.get(f'http://numbersapi.com/{number}')
        await interaction.response.send_message(f'{response.text}')

    @commands.hybrid_command(
        name="gaming",
        description="Test command before going live")
    async def gaming(self, ctx,
                     hours: Optional[int], minutes: Optional[int],
                     seconds: Optional[int], games: Optional[str]) -> None:

        if hours is None and minutes is None and seconds is None:
            hours = 1
        if minutes is None:
            minutes = 0
        if seconds is None:
            seconds = 0

        relative_time = convert_to_unix_time_relative(0, hours, minutes, seconds)
        actual_time = convert_to_unix_time(0, hours, minutes, seconds)

        await ctx.send(f"{ctx.author.mention} has requested all the "
                       f"{r.choice(self.bot.names)}'s to play {games} at {actual_time} which is {relative_time}")


async def setup(bot):
    await bot.add_cog(Facts(bot))
