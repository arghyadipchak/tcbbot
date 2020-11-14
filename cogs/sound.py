from discord.ext import commands

class Sound(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="join")
    async def join(self, ctx):
        vc = ctx.guild.voice_client
        if vc and vc.is_connected():
            await vc.move_to(ctx.author.voice.channel)
        else:
            await ctx.author.voice.channel.connect()

    @commands.command(name="leave")
    async def leave(self, ctx):
        vc = ctx.guild.voice_client
        if vc and vc.is_connected():
            await vc.disconnect()