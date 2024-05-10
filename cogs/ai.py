import discord
from discord.ext import commands

import pathlib
import textwrap

import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown

import config

api_key = config.GOOGLE_API
genai.configure(api_key=api_key)

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE"
  },
]


def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


class ai(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('AI commands are loaded')

    @commands.hybrid_command(
        name="ai",
        description="Uses Google Gemini AI to provide responses.")
    async def ai(self, ctx: commands.Context, *, prompt: str):
        # noinspection PyTypeChecker
        model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                      generation_config=generation_config,
                                      safety_settings=safety_settings)
        response = model.generate_content(f'{prompt}')
        await ctx.reply(response.text)


async def setup(bot):
    await bot.add_cog(ai(bot))
