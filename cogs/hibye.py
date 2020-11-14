from discord.ext import commands

class HiBye(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="hello")
    async def hello(self, ctx: commands.Context):
        await ctx.send(f"Hello {ctx.author.mention}! I'm the TCB Bot.")

    @commands.command(name="bye")
    async def bye(self, ctx: commands.Context):
        await ctx.send(f"Bye Bye {ctx.author.mention}!")