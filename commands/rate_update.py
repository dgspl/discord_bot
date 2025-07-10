from discord.ext import commands

class RateUpdate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="rate_update")
    async def rate_update(self, ctx):
        await ctx.send("/rate_update コマンドは実装予定です。")