import discord
from discord.ext import commands
import os
import random


class Brendan(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.image_path = './images/brendan'
        # Cache available images on load
        self.available_images = self._get_available_images()

    def _get_available_images(self) -> list:
        """Get list of available Brendan images"""
        images = []
        if os.path.exists(self.image_path):
            images = [f for f in os.listdir(self.image_path) if f.endswith('.png')]
        return images

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Brendan command loaded ({len(self.available_images)} images)')

    @commands.hybrid_command(
        name="bgay",
        description="Random image of the gay boy."
    )
    async def bgay(self, ctx: commands.Context):
        """Send a random Brendan image"""
        if not self.available_images:
            await ctx.send("❌ No images found!")
            return
            
        random_image = random.choice(self.available_images)
        image_path = os.path.join(self.image_path, random_image)
        
        try:
            await ctx.send(file=discord.File(image_path))
        except FileNotFoundError:
            await ctx.send("❌ Image file not found!")


async def setup(bot):
    await bot.add_cog(Brendan(bot))