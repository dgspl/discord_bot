import discord
from discord.ext import commands
import asyncio
import os

from commands import kurupo, rate_update, monthly_news

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="/", intents=intents)

async def setup():
    await bot.add_cog(kurupo.Kurupo(bot))
    await bot.add_cog(rate_update.RateUpdate(bot))
    await bot.add_cog(monthly_news.MonthlyNews(bot))

async def main():
    await setup()
    token = os.getenv("DISCORD_TOKEN")
    if not token:
        raise ValueError("DISCORD_TOKEN が環境変数に設定されていません。")
    await bot.start(token)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"Botの起動中にエラーが発生しました: {e}")
