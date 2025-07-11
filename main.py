import discord
import os
import asyncio

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'✅ Bot is logged in as {client.user}')

async def run_bot():
    try:
        await client.start(TOKEN)
    except Exception as e:
        print(f"⚠️ Bot crashed with error: {e}")
        await asyncio.sleep(60)  # 1分待って再起動（連続クラッシュ防止）
        await run_bot()

if __name__ == "__main__":
    asyncio.run(run_bot())
