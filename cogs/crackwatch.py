import discord
from discord.ext import commands
import os, re
from pymongo import MongoClient

class CrackWatch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        USER = os.getenv('DB_USER')
        PASSWORD = os.getenv('DB_PASSWORD')
        DB = os.getenv('DB_NAME')
        self.db_client = MongoClient(username = USER, password = PASSWORD, authSource = DB)
        self.db = self.db_client[DB]

    def find_game(self, gname):
        gslug = '-'.join(re.findall(r"[a-z0-9]+", gname.lower()))
        games = self.db.allgames
        return games.find_one({'slug': gslug})

    @commands.command(name="crack")
    async def crack(self, ctx, *args):
        gname = ' '.join(args)
        if args:
            game = self.find_game(gname)
            if game:
                emb = discord.Embed(title = game['title'])
                emb.add_field(name = "Crack Status:", value = game['crackStatus'])
                emb.set_image(url = game['image'])
                await ctx.send(embed = emb)
            else:
                await ctx.send(f"{gname}: Not Found!")
        else:
            await ctx.send("Please Enter Game!")