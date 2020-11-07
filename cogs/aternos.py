from discord.ext import commands

class Aternos(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="aternos")
    async def hello(self, ctx, *args):
        if args:
            work = args[0]
            if work=='start':
                pass    #Launch Server
            elif work=='status':
                pass    #Show Server Status
            elif work=='players':
                pass    #Show Players
            elif work=='stop':
                pass    #Stop Server
            else:
                await ctx.send("Invalid Command!")
        else:
            await ctx.send("Invlid Command!")