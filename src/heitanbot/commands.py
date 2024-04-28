import discord
from discord import app_commands

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
