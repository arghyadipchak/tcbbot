import discord
from discord.ext import commands
import os
from pymongo import MongoClient

class CrackWatch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        USER = os.getenv('DB_USER')
        PASSWORD = os.getenv('DB_PASSWORD')
        DB = os.getenv('DB_NAME')
        self.db_client = MongoClient(username = USER, password = PASSWORD, authSource = DB)
        self.db = self.db_client[DB]

    def find_game(self, *gwords):
        gtmp = list(gwords)
        for i in range(len(gtmp)):
            gtmp[i] = ''.join(c for c in gtmp[i] if c.isalnum())
        gslug = '-'.join(gtmp).lower()
        #gname = ' '.join(gwords)

        games = self.db.allgames
        return games.find_one({'slug': gslug})

    @commands.command(name="crack")
    async def crack(self, ctx, *args):
        if args:
            game = self.find_game(*args)
            if game:
                emb = discord.Embed(title = game['title'])
                emb.add_field(name = "Crack Status:", value = game['crackStatus'])
                emb.set_image(url = game['image'])
                await ctx.send(embed = emb)
            else:
                await ctx.send(f"{' '.join(args)}: Not Found!")
        else:
            await ctx.send("Please Enter Game!")