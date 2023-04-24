import asyncio
import random as r
from datetime import datetime, timedelta
from typing import Optional
import discord
from discord import app_commands
import pytz
from discord.ext import commands


class letsGoing(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.lgmention = 749257590520807455
        self.yes = '<:approved:773090431416139777>'
        self.later = '<:maybe:792601596797648926>'
        self.no = '<:disapproved:773090453850423317>'
        self.polls = []
        self.members = {}

    async def reset_poll(self, hours, message):
        await asyncio.sleep(hours * 3600)
        await message.edit(
            embed=discord.Embed(title="Lets Going?",
                                description=f"This poll is over.",
                                colour=r.choice(self.bot.colour_list),
                                timestamp=datetime.utcnow()
                                ))
        self.polls = []
        self.members = {}

    @commands.Cog.listener()
    async def on_ready(self):
        print('Lets going command is loaded')

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        user = payload.member
        if payload.guild_id is None:
            return
        else:
            if payload.message_id in self.polls:
                if not payload.member.bot:
                    if user not in self.members:
                        self.members.update({user: 0})

                    elif self.members[user] == 3:
                        await self.bot.get_channel(payload.channel_id).send(
                            f'{user.mention} fuck off and stop pressing the buttons you fucking moron.')
                        self.members[user] = (self.members[user] + 1)

                    elif self.members[user] > 3:
                        return

                    if self.members[user] < 4:
                        self.members[user] = (self.members[user] + 1)
                        if str(payload.emoji) == str(self.yes):
                            await self.bot.get_channel(payload.channel_id).send(
                                f'{user.mention} has said ***YES*** to the lets going request.')
                            return
                        elif str(payload.emoji) == str(self.later):
                            await self.bot.get_channel(payload.channel_id).send(
                                f'{user.mention} has said ***LATER*** to the lets going request.')
                            return
                        elif str(payload.emoji) == str(self.no):
                            await self.bot.get_channel(payload.channel_id).send(
                                f'{user.mention} has said ***NO*** to the lets going request.')
                            return
                        else:
                            return

    @commands.command(name="letsgoing")
    async def letsgoing(self, ctx, *games: Optional[str]):
        tz_Aus = datetime.now(pytz.timezone('Australia/Sydney')) + timedelta(hours=1)
        later_t = tz_Aus.strftime('%I:%M %p')
        arg_count = len(games)
        print(f'{games} games')
        print(f'{arg_count} arg count')
        game_string = ""

        for game in games:
            print(f'{game} game')
            game_string += game + " "

        options = ("Yes", "Later", "No")
        emoji_options = (self.yes, self.later, self.no)

        if arg_count <= 0:
            embed = discord.Embed(title="Lets Going?",
                                  description=f"{ctx.author.mention} has asked if you be available for a lets going?",
                                  colour=r.choice(self.bot.colour_list),
                                  timestamp=datetime.now(pytz.timezone('Australia/Sydney')))
        else:
            game_string = game_string[:-1]
            embed = discord.Embed(title=f"Lets Going in {game_string}?",
                                  description=f"{ctx.author.mention} has asked if you be available for a lets going?",
                                  colour=r.choice(self.bot.colour_list),
                                  timestamp=datetime.now(pytz.timezone('Australia/Sydney')))
        fields = [("Options", "\n".join([f"{emoji_options[idx]} {option}" for idx, option in enumerate(options)]),
                   False)]
        
        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)
        embed.set_footer(text=f"Stopping poll at {later_t}")

        await ctx.send(f'{discord.utils.get(ctx.guild.roles, id=self.lgmention).mention}')
        message = await ctx.send(embed=embed)

        for emoji in emoji_options[:len(options)]:
            await message.add_reaction(emoji)

        self.polls = list((message.channel.id, message.id))
        self.members = {}
        await self.reset_poll(1, message)

    @commands.command(name="lg")
    async def lg(self, ctx, *games: Optional[str]):
        tz_Aus = datetime.now(pytz.timezone('Australia/Sydney')) + timedelta(hours=1)
        later_t = tz_Aus.strftime('%I:%M %p')
        arg_count = len(games)
        game_string = ""

        for game in games:
            game_string += game + ""

        options = ("Yes", "Later", "No")
        emoji_options = (self.yes, self.later, self.no)

        if arg_count <= 0:
            embed = discord.Embed(title="Lets Going?",
                                  description=f"{ctx.author.mention} has asked if you be available for a lets going?",
                                  colour=r.choice(self.bot.colour_list),
                                  timestamp=datetime.now(pytz.timezone('Australia/Sydney')))
        else:
            game_string = game_string[:-1]
            embed = discord.Embed(title=f"Lets Going in {game_string}?",
                                  description=f"{ctx.author.mention} has asked if you be available for a lets going?",
                                  colour=r.choice(self.bot.colour_list),
                                  timestamp=datetime.now(pytz.timezone('Australia/Sydney')))
        fields = [("Options", "\n".join([f"{emoji_options[idx]} {option}" for idx, option in enumerate(options)]),
                   False)]

        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)
        embed.set_footer(text=f"Stopping poll at {later_t}")

        await ctx.send(f'{discord.utils.get(ctx.guild.roles, id=self.lgmention).mention}')
        message = await ctx.send(embed=embed)

        for emoji in emoji_options[:len(options)]:
            await message.add_reaction(emoji)

        self.polls = list((message.channel.id, message.id))
        self.members = {}
        await self.reset_poll(1, message)


async def setup(bot):
    await bot.add_cog(letsGoing(bot))
