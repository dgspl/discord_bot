import discord
from discord.ext import commands, tasks
import os
import asyncio

from commands import kurupo, rate_update, monthly_news

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="/", intents=intents)

@tasks.loop(minutes=15)
async def keep_alive_log():
    print("✅ Bot is alive and running...")

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"🔁 Synced {len(synced)} command(s)")
    except Exception as e:
        print(f"❌ Failed to sync commands: {e}")
    keep_alive_log.start()

async def main():
    await bot.add_cog(kurupo.Kurupo(bot))
    await bot.add_cog(rate_update.RateUpdate(bot))
    await bot.add_cog(monthly_news.MonthlyNews(bot))
    
    token = os.environ.get("DISCORD_TOKEN")  # .envを読み込まないのでRender用
    if not token:
        raise ValueError("DISCORD_TOKEN is not set.")
    
    await bot.start(token)

if __name__ == "__main__":
    asyncio.run(main())
