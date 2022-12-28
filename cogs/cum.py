import sys
import discord
from discord.ext import commands
from typing import Optional


class Cum(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Cum command is loaded')

    @commands.command()
    async def cum(self, ctx, amount: Optional[str]):
        """This command sends the cummies. No number will send a default 1 Cum."""
        emoji = '<:cum:702822392371740684>'
        try:
            if amount is None:
                await ctx.send(str(emoji) * 1)
            elif int(amount) <= 50:
                await ctx.send(str(emoji) * int(amount))
            elif int(amount) == 69:
                await ctx.send(
                    f"Nice\n                                          "
                    f"{str(emoji)}\n                                    "
                    f"{str(emoji)}{str(emoji)}{str(emoji)}\n                              "
                    f"{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}\n                        "
                    f"{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}"
                    f"\n                  {str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}"
                    f"{str(emoji)}{str(emoji)}{str(emoji)}\n            {str(emoji)}{str(emoji)}{str(emoji)}"
                    f"{str(emoji)}"
                    f"{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}\n"
                    f"      {str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}"
                    f"{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}\n"
                    f"{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}"
                    f"{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}"
                )
            elif int(amount) > 50 & int(amount) != 69:
                await ctx.send(
                    f"My balls are only of limited size, to produce '{amount}' cummies, i would need to consult"
                    f" with harris to learn how to cum that much.")
        except ValueError:
            await ctx.send(f"Try using a number next time bucko")
        except:
            await ctx.send(f'Inform Harris that you are fucking retarded and to tell him this: {sys.exc_info()}')


async def setup(bot):
    await bot.add_cog(Cum(bot))
