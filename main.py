import discord
from discord.ext import commands
import os
from commands import kurupo, rate_update, monthly_news

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True
intents.voice_states = True

bot = commands.Bot(command_prefix="/", intents=intents)

# Load commands
bot.add_cog(kurupo.Kurupo(bot))
bot.add_cog(rate_update.RateUpdate(bot))
bot.add_cog(monthly_news.MonthlyNews(bot))

@bot.event
async def on_ready():
    print(f"Bot is ready. Logged in as {bot.user}")

bot.run(os.getenv("DISCORD_TOKEN"))