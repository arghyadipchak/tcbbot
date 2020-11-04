import discord, asyncio
from discord.ext.commands import Bot
from cogs.hibye import *
from cogs.crackwatch import *

def get_token():
    import pickle
    with open("token.p",'rb') as fh:
        return pickle.load(fh)
    return None

bot = Bot('?')
bot.add_cog(HiBye(bot))
bot.add_cog(CrackWatch(bot))

bot.run(get_token())