import discord
from discord.ext import commands, tasks

import os
import aiohttp
import asyncio

from typing import Optional, Literal

# Loading .env files
from dotenv import load_dotenv
load_dotenv()
# ===================================================================================
# Bot Setup

intents = discord.Intents.default()
intents.message_content = True

default_prefix = "."
# bot = commands.Bot(command_prefix=default_prefix,intents=intents)

class ArcanideBot(commands.Bot):
	def __init__(self):
		super().__init__(
			command_prefix=default_prefix,
			intents=intents,
			activity=discord.Game(name='with AR7')
		)
	
	async def setup_hook(self):
		# await self.background_task.start()
		for filename in os.listdir("./cogs"):
			if filename.endswith(".py"):
				await self.load_extension(f"cogs.{filename[:-3]}")

	async def on_ready(self):
		print(f"Logged in as {self.user.name}#{self.user.discriminator}")

bot = ArcanideBot()

@bot.command()
@commands.guild_only()
@commands.is_owner()
async def sync(ctx: commands.Context, guilds: commands.Greedy[discord.Object], spec: Optional[Literal["~", "*", "^"]] = None) -> None:
    if not guilds:
        if spec == "~":
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "*":
            ctx.bot.tree.copy_global_to(guild=ctx.guild)
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "^":
            ctx.bot.tree.clear_commands(guild=ctx.guild)
            await ctx.bot.tree.sync(guild=ctx.guild)
            synced = []
        else:
            synced = await ctx.bot.tree.sync()

        await ctx.send(
            f"Synced {len(synced)} commands {'globally' if spec is None else 'to the current guild.'}"
        )
        return

    ret = 0
    for guild in guilds:
        try:
            await ctx.bot.tree.sync(guild=guild)
        except discord.HTTPException:
            pass
        else:
            ret += 1

    await ctx.send(f"Synced the tree to {ret}/{len(guilds)}.")
# ===================================================================================
TOKEN = os.getenv('discord_token')
async def main():
	async with bot:
		await bot.start(TOKEN)

asyncio.run(main())
# bot.run(TOKEN,reconnect=True)