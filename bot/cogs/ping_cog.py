
import discord
from discord.ext import commands
import time


class PingCog(commands.Cog):
    """
    A cog to allow the bot to test the latency between call and response of a command.
    """
    def __init__(self, bot) -> None:
        self.bot = bot
    
    @commands.command()
    async def ping(self, ctx):
        t = time.time()
        await ctx.trigger_typing()
        t2 = round((time.time() - t) * 1000)
        await ctx.send(f'Pong! Response in {t2}ms')


def setup(bot):
    bot.add_cog(PingCog(bot))