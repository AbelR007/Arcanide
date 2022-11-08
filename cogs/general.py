import discord
from discord.ext import commands

# General Cog

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")
    
    @commands.command()
    async def invite(self, ctx):
        embed = discord.Embed(
            title = "Invite Arcanide to your server",
            description = "[Click this link to invite](https://discord.com/api/oauth2/authorize?client_id=1034403556251410472&permissions=139586829376&scope=bot)",
            color = discord.Color.green()
        )
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(General(bot))
