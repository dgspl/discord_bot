from discord.ext import commands

class Kurupo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="kurupo")
    async def kurupo(self, ctx):
        await ctx.send("/kurupo コマンドは実装予定です。")