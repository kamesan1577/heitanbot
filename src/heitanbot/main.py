import discord
from discord.ext import commands
import os
import config
from commands import setup

intents = discord.Intents.all()
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix="/", intents=intents, case_insensitive=True)

setup(bot)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    await bot.tree.sync()

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    await bot.process_commands(message)

bot.run(config.DISCORD_TOKEN)
