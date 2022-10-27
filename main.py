import discord
from discord.ext import commands, tasks

import os
import aiohttp
import asyncio

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
# ===================================================================================
TOKEN = os.getenv('discord_token')
async def main():
	async with bot:
		await bot.start(TOKEN)

asyncio.run(main())
# bot.run(TOKEN,reconnect=True)