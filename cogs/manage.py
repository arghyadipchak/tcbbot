from discord.ext import commands
from os import path, system
from git import Repo

class Manage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="update")
    async def update(self, ctx: commands.Context):
        repo = Repo(path.dirname(path.dirname(__file__)))
        repo.remotes.origin.pull()
        await ctx.send("Updating...")
        system("pm2 restart tcbbot")