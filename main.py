import discord
import config
import asyncio
import os
import logging
from discord.ext import commands

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('discord')

intents = discord.Intents.default()
intents.message_content = True  # Enable if you need message content
bot = commands.Bot(command_prefix='.', intents=intents)

# Bot attributes
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
bot.colour_list = list(bot.colours.values())  # More explicit conversion
bot.lets_going_timer = 6


@bot.event
async def on_ready():
    logger.info(f'Bot is online as {bot.user.name} (ID: {bot.user.id})')
    logger.info(f'Connected to {len(bot.guilds)} guilds')


# Remove this redundant event handler - it doesn't work as intended
# The bot.process_commands is being called incorrectly anyway


async def load_extensions():
    """Load all cogs from the cogs directory"""
    cogs_loaded = 0
    cogs_failed = 0
    
    for file in os.listdir('./cogs'):
        if file.endswith('.py'):
            try:
                await bot.load_extension(f'cogs.{file[:-3]}')
                cogs_loaded += 1
                logger.info(f'Loaded cog: {file[:-3]}')
            except Exception as e:
                cogs_failed += 1
                logger.error(f'Failed to load cog {file[:-3]}: {e}')
    
    logger.info(f'Loaded {cogs_loaded} cogs, {cogs_failed} failed')


async def main():
    async with bot:
        await load_extensions()
        await bot.start(config.TOKEN)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info('Bot shutdown requested')
