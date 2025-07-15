from discord.ext import commands
from discord import app_commands, Interaction

class Kurupo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="kurupo", description="kurupoコマンドのテスト")
    async def kurupo(self, interaction: Interaction):
        await interaction.response.send_message("/kurupo コマンドは実装予定です。")
