from logging import getLogger
from api import HeitanAPI
import discord
from discord import app_commands

logger = getLogger(__name__)

def setup(bot):
    tree = bot.tree

    @tree.command(name="help", description="ヘルプを表示します")
    async def help(interaction: discord.Interaction):
        help_message = "```"
        for command in sorted(tree.get_commands(), key=lambda c: c.name):
            help_message += f"/{command.name}: {command.description}\n\n"

        help_message += "```"
        embed = discord.Embed(title="コマンド一覧(アルファベット順)", color=0x00ff00, description=help_message)
        await interaction.response.send_message(embed=embed)

    @tree.command(name="moderate", description="テキストを適切な表現に変換します")
    @app_commands.describe(text="変換するテキスト or 変換するメッセージへのリンク")
    async def moderate(interaction: discord.Interaction, text: str):
        await interaction.response.defer()
        try:
            heitanAPI = HeitanAPI()
            if "https://discord.com/channels/" in text:
                link = text.split("https://discord.com/channels/")[1]
                guild_id, channel_id, message_id = map(int, link.split("/"))

                if interaction.guild.id != guild_id:
                    return
                target_message = await bot.get_channel(channel_id).fetch_message(message_id)

                text = target_message.content

            moderated_text = await heitanAPI.moderate(text)

            await interaction.followup.send(moderated_text)
        except Exception as e:
            logger.error(f"Error: {e}")
            await interaction.followup.send("エラーが発生しました")

    @tree.command(name="is_safe", description="テキストが適切な表現かどうかを判定します")
    @app_commands.describe(text="判定するテキスト or 判定するメッセージへのリンク")
    async def is_safe(interaction: discord.Interaction, text: str):
        await interaction.response.defer()
        original_text = text
        try:
            heitanAPI = HeitanAPI()
            if "https://discord.com/channels/" in text:
                link = text.split("https://discord.com/channels/")[1]
                guild_id, channel_id, message_id = map(int, link.split("/"))

                if interaction.guild.id != guild_id:
                    return
                target_message = await bot.get_channel(channel_id).fetch_message(message_id)
                text = target_message.content

            is_safe = await heitanAPI.is_required_moderation(text)
            await interaction.followup.send(f"{original_text} は適切な表現です" if not is_safe else f"{original_text} は適切な表現ではありません")


        except Exception as e:
            logger.error(f"Error: {e}")
            await interaction.followup.send("エラーが発生しました")
