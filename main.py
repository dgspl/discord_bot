import discord
from discord.ext import commands
import asyncio
import os

from commands import kurupo, rate_update, monthly_news

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="/", intents=intents)

async def main():
    await bot.add_cog(kurupo.Kurupo(bot))
    await bot.add_cog(rate_update.RateUpdate(bot))
    await bot.add_cog(monthly_news.MonthlyNews(bot))
    await bot.start(os.getenv("DISCORD_TOKEN"))

if __name__ == "__main__":
    asyncio.run(main())