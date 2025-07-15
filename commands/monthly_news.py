from discord.ext import commands
from discord import app_commands, Interaction

class MonthlyNews(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="monthly_news", description="月次ニュースを表示します")
    async def monthly_news(self, interaction: Interaction):
        await interaction.response.send_message("月次ニュースは現在準備中です。")
