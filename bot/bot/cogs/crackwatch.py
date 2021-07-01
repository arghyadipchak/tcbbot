import discord, asyncio
from discord.ext import commands
from os import getenv
from pymongo import MongoClient
import re

class CrackWatch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        HOST = getenv('DB_HOST')
        PORT = getenv('DB_PORT')
        USER = getenv('DB_USER')
        PSWD = getenv('DB_PASSWORD')
        AUTH = getenv('DB_AUTH')
        DB = getenv('DB_WORK')
        self.db_client = MongoClient(host = HOST, port = PORT, username = USER, password = PSWD, authSource = AUTH)
        self.db = self.db_client[DB]

    def find_games(self, gname):
        gslug = '-'.join(re.findall(r"[a-z0-9]+", gname.lower()))
        games = self.db.allgames
        return list(games.find({'slug': {'$regex' : f".*{gslug}.*"}})[:10])

    def get_embed(self, game):
        if game:
            emb = discord.Embed(title = game['title'])
            emb.add_field(name = "Crack Status:", value = game['crackStatus'])
            emb.set_image(url = game['image'])
            return emb
        else:
            return discord.Embed()

    @commands.command(name="crack")
    async def crack(self, ctx: , *args):
        gname = ' '.join(args)
        if args:
            games = self.find_games(gname)
            if games:
                c = 0
                ng = len(games)
                msg = await ctx.send(embed = self.get_embed(games[c]))
                if ng==1: return

                await msg.add_reaction("⬅")
                await msg.add_reaction("➡")
                await msg.add_reaction("☑")

                def reaction_check(reaction, user):
                    return user!=self.bot.user and reaction.message==msg and (str(reaction.emoji)=="⬅" or str(reaction.emoji)=="➡" or str(reaction.emoji)=="☑")

                while True:
                    try:
                        reaction, user = await self.bot.wait_for('reaction_add', timeout = 120.0, check = reaction_check)
                    except asyncio.TimeoutError:
                        break
                    else:
                        if str(reaction.emoji)=="⬅":
                            c = (c-1)%ng
                        elif str(reaction.emoji)=="➡":
                            c = (c+1)%ng
                        else:
                            break
                        await msg.remove_reaction(reaction, user)
                        await msg.edit(embed = self.get_embed(games[c]))
                await msg.clear_reactions()
                
            else:
                await ctx.send("Nothing Found!")
        else:
            await ctx.send("Please Enter Game!")