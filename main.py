import discord
import config
import asyncio
import os
from discord.ext import commands

intents = discord.Intents.default()
# intents.message_content = False
bot = commands.Bot(command_prefix=commands.when_mentioned, intents=intents)
bot.names = ['squirt', 'champ', 'sport', 'cob', 'cobsta', 'bucko', 'fucktard', 'cunt', 'cock eater', 'kid fucker']
bot.colours = {
    'WHITE': 0xFFFFFF,
    'AQUA': 0x1ABC9C,
    'GREEN': 0x2ECC71,
    'BLUE': 0x3498DB,
    'PURPLE': 0x9B59B6,
    'LUMINOUS_VIVID_PINK': 0xE91E63,
    'GOLD': 0xF1C40F,
    'ORANGE': 0xE67E22,
    'RED': 0xE74C3C,
    'NAVY': 0x34495E,
    'DARK_AQUA': 0x11806A,
    'DARK_GREEN': 0x1F8B4C,
    'DARK_BLUE': 0x206694,
    'DARK_PURPLE': 0x71368A,
    'DARK_VIVID_PINK': 0xAD1457,
    'DARK_GOLD': 0xC27C0E,
    'DARK_ORANGE': 0xA84300,
    'DARK_RED': 0x992D22,
    'DARK_NAVY': 0x2C3E50
}
bot.colour_list = [c for c in bot.colours.values()]


@bot.event
async def on_ready():
    print('Online.')


@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if not (message.content.split(' ', 1)[0]) == (f'<@{bot.user.id}>'):
        return
    if message.author.id == bot.user.id:
        return
    await bot.process_commands(message.content)


async def load():
    for file in os.listdir('./cogs'):
        if file.endswith('.py'):
            await bot.load_extension(f'cogs.{file[:-3]}')


async def main():
    await load()
    await bot.start(config.TOKEN, reconnect=True)


asyncio.run(main())
