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
    #Token not included for security purposes. To use this code for your own bot, you can insert your own bot token in the below sector
    await bot.start("")

asyncio.run(main())
