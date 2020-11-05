import discord
from discord.ext import commands
from pymongo import MongoClient

def find_game(*gwords):
  # gtmp = list(gwords)
  # for i in range(len(gtmp)):
  #   gtmp[i] = ''.join(c for c in gtmp[i] if c.isalnum())
  # gslug = '-'.join(slt)
  gname = ' '.join(gname)

  client = MongoClient()
  games = client.crackwatch.allgames

  return games.find_one({'title': gname})

class CrackWatch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="crack")
    async def crack(self, ctx, *args):
        game = find_game(args)
        if game:
            emb = discord.Embed(title = game['title'])
            emb.add_field(name = "Crack Status:", value = game['crackStatus'])
            emb.set_image(url = game['image'])
            await ctx.send(embed = emb)
        else:
            await ctx.send(f"{' '.join(args)}: Not Found!")