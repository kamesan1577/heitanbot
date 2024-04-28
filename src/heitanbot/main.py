
import os
from logging import getLogger, basicConfig, DEBUG, INFO
import config
from bot_commands import setup
from bot_actions import moderate_if_is_unsafe
import discord
from discord.ext import commands

logger = getLogger(__name__)
logger.setLevel(INFO)
if config.IS_DEV:
    logger.setLevel(DEBUG)


intents = discord.Intents.all()
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix=config.prefix, intents=intents, case_insensitive=True)

setup(bot)

@bot.event
async def on_ready():
    logger.info(f"Logged in as {bot.user.name}")
    await bot.tree.sync()

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    await bot.process_commands(message)

    if not any(message.content.startswith(prefix) for prefix in [config.prefix, "http", "https","www","!"]):
        logger.debug(f"message length: { len(message.content) }")
        if len(message.content) < 400:
            await moderate_if_is_unsafe(bot, message)

bot.run(config.DISCORD_TOKEN)

