from api import HeitanAPI
import discord
from logging import getLogger

logger = getLogger(__name__)


async def moderate_if_is_unsafe(bot, message):
    heitanAPI = HeitanAPI()
    try:
        if await heitanAPI.is_required_moderation(message.content):
            logger.info(f"Moderating message: {message.content}")

            embed = discord.Embed(
                title="メッセージが修正されました",
                description=f"{message.author.display_name}@{message.author.name}",
                color=0xFF0000,
            )
            moderated_text = await heitanAPI.moderate(message.content)
            embed.add_field(
                name="修正前:", value=f"||{message.content}||", inline=False
            )
            embed.add_field(name="修正後:", value=moderated_text, inline=False)
            await message.channel.send(embed=embed)
            await message.delete()
        return
    except Exception as e:
        logger.error(f"Error: {e}")
        return
