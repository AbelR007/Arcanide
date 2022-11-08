import discord
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command(
        description = "Add a character",
    )
    @commands.is_owner()
    async def addchar(self, ctx: commands.Context, char: str) -> None:
        await ctx.send(f"Adding character {char}")
        
    
async def setup(bot: commands.Bot):
    await bot.add_cog(Admin(bot))