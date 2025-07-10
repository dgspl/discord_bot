from discord.ext import commands

class MonthlyNews(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="monthly_news")
    async def monthly_news(self, ctx):
        await ctx.send("/monthly_news コマンドは実装予定です。")