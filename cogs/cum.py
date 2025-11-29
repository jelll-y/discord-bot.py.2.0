import discord
from discord.ext import commands
from typing import Optional


class Cum(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.emoji = '<:cum:702822392371740684>'
        self.max_amount = 50

    @commands.Cog.listener()
    async def on_ready(self):
        print('Cum command loaded')

    @commands.hybrid_command(
        name="cum",
        description="Sends cummies. No number sends 1 cum."
    )
    async def cum(self, ctx: commands.Context, amount: Optional[str] = None):
        """Send cum emojis"""
        try:
            # Convert to int or use default
            if amount is None:
                num_amount = 1
            else:
                num_amount = int(amount)
            
            # Check for 69 BEFORE checking the range
            if num_amount == 69:
                await ctx.send(self._nice_pattern())
            # Check if within normal range
            elif 1 <= num_amount <= self.max_amount:
                await ctx.send(self.emoji * num_amount)
            # Check if over the limit (and not 69)
            elif num_amount > self.max_amount:
                await ctx.send(
                    f"My balls are only of limited size, to produce '{num_amount}' cummies, i would need to consult"
                    f" with harris to learn how to cum that much.")
            else:
                await ctx.send(f"Invalid amount!")
                
        except ValueError:
            await ctx.send("Try using a number next time bucko")

    def _nice_pattern(self) -> str:
        """Generate the 69 pattern"""
        e = self.emoji
        return (
            f"Nice\n"
            f"                                          {e}\n"
            f"                                    {e*3}\n"
            f"                              {e*5}\n"
            f"                        {e*7}\n"
            f"                  {e*9}\n"
            f"            {e*11}\n"
            f"      {e*13}\n"
            f"{e*15}"
        )


async def setup(bot):
    await bot.add_cog(Cum(bot))