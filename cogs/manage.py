from discord.ext import commands
from os import path
#from git import Repo

class Manage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="update")
    async def update(self, ctx: commands.Context):
        await ctx.send(path.dirname(__file__))
    #repo = Repo(os.path.realpath(__file__))