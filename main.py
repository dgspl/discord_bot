import discord
from discord.ext import commands
import asyncio
import os
from dotenv import load_dotenv  # ← 追加

from commands import kurupo, rate_update, monthly_news

load_dotenv()  # ← 追加

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is logged in as {bot.user}")

async def main():
    await bot.add_cog(kurupo.Kurupo(bot))
    await bot.add_cog(rate_update.RateUpdate(bot))
    await bot.add_cog(monthly_news.MonthlyNews(bot))
    await bot.start(os.getenv("DISCORD_TOKEN"))

if __name__ == "__main__":
    asyncio.run(main())
