import discord
from discord.ext import commands

def find_game(string):
  import requests

  parameter = {'is_released':'true'}

  request = requests.get('https://api.crackwatch.com/api/games', parameter)

  ##print(request.text)

  request_json=request.json()
  # print(request_json)
  # for i in range(0,len(request_json)):
  #   print(request_json[i]['title'])

  ##string='Devil May Cry 6'

  slt = string.lower().split()
  for i in range(len(slt)):
    slt[i] = ''.join(e for e in slt[i] if e.isalnum())
  text = '-'.join(slt)
  print(text)

  for i in range(0,len(request_json)):
    if(request_json[i]['slug']==text):
      return request_json[i]['image']

class CrackWatch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="crack")
    async def crack(self, ctx, *args):
        game = ' '.join(args)
        img = find_game(game)
        if img:
            emb = discord.Embed()
            emb.set_image(url=img)
            await ctx.send(embed=emb)
        else:
            await ctx.send(f"{game}: Not Found!")