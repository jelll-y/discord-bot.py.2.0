import discord
from discord.ext import commands
import os
from typing import Optional
import random as r


class Mms(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('MMS command is loaded')

    @commands.command()
    async def mms(self, ctx, value: Optional[str] = None):
        try:
            if value is None:
                mms_img = os.path.abspath('.//mms/mms0.png')
                await ctx.send(file=discord.File(mms_img))
            if int(value) <= 10:
                mms_img = os.path.abspath('.//mms/mms' + str(value) + '.png')
                await ctx.send(file=discord.File(mms_img))
            elif 10 < int(value) <= 100:
                await ctx.send(f"You seem to be just a tad minged, this is the best i can do "
                               f"{r.choice(self.bot.names)}.")
                mms_img = os.path.abspath('.//mms/mms10.png')
                await ctx.send(file=discord.File(mms_img))
            elif int(value) > 100:
                await ctx.send(f"Holy fuck, you sir, are quite minged. I don't have a scale that goes that high, "
                               f"have this instead {r.choice(self.bot.names)}.")
                mms_img = os.path.abspath('.//mms/mms10.png')
                await ctx.send(file=discord.File(mms_img))
        except ValueError:
            await ctx.send(f"You seem a bit slow in the head because '{value}' is not a number.")


async def setup(bot):
    await bot.add_cog(Mms(bot))
