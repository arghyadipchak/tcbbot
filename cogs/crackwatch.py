import discord, asyncio
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
    async def crack(self, ctx: commands.Context, *args):
        print(ctx.message)
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