import asyncio
import os
import discord
from discord.ext import commands

intents= discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix="$", intents=intents, help_command=None)

async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

async def main():
    await load()
    await bot.start("")

asyncio.run(main())