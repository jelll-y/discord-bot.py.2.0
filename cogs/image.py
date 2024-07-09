import discord
from discord.ext import commands
import config
import os

import textwrap
from openai import OpenAI
os.environ["OPENAI_API_KEY"] = config.CHATGPT_API
client = OpenAI()


def response(prompt):
    ai_image = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1
    )
    print(ai_image)
    return ai_image.data[0].url


class image(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Image commands are loaded')

    @commands.command(
        name='image',
        description="Uses ChatGPT AI for image generation.")
    async def image(self, ctx: commands.Context, *, prompt: str):
        img_obj_string = str(response(prompt))
        print(textwrap.fill(img_obj_string, width=140))


async def setup(bot):
    await bot.add_cog(image(bot))
