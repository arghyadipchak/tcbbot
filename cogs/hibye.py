from discord.ext import commands

class HiBye(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="hello")
    async def hello(self, ctx):
        await ctx.send("Hello I'm the TCB Bot! I can't do anything yet, but I will soon.")

    @commands.command(name="bye")
    async def bye(self, ctx):
        await ctx.send(f"Bye Bye {ctx.author.mention}!")