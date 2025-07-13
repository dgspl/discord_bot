import discord
from discord.ext import commands, tasks
import os
import asyncio

# ローカル用に .env を読み込み
if not os.getenv("RENDER"):
    from dotenv import load_dotenv
    load_dotenv()

from commands import kurupo, rate_update, monthly_news

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="/", intents=intents)

@tasks.loop(minutes=15)
async def keep_alive_log():
    print("✅ Bot is alive and running...")

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    keep_alive_log.start()

async def main():
    await bot.add_cog(kurupo.Kurupo(bot))
    await bot.add_cog(rate_update.RateUpdate(bot))
    await bot.add_cog(monthly_news.MonthlyNews(bot))

    token = os.getenv("DISCORD_TOKEN")
    if token is None:
        raise RuntimeError("❌ DISCORD_TOKEN が設定されていません")
    await bot.start(token)

if __name__ == "__main__":
    asyncio.run(main())
