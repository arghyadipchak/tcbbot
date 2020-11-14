from discord.ext import commands
from discord.utils import get
from spotipy.oauth2 import SpotifyClientCredentials

class Sound(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="join")
    async def join(self, ctx: commands.Context, *, channel: discord.VoiceChannel = None):
        if not channel:
            channel = ctx.author.voice.channel
        else:
            channel =  ctx.author.voice.channel
        if channel:
            vc = ctx.guild.voice_client
            if vc and vc.is_connected():
                await vc.move_to(channel)
            else:
                await channel.connect()
        else:
            await ctx.send("Please mention a VC or connect to a VC!")

    @commands.command(name="leave")
    async def leave(self, ctx: commands.Context):
        vc = ctx.guild.voice_client
        if vc and vc.is_connected():
            await vc.disconnect()