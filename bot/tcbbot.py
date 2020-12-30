from cogs import *
from discord.ext.commands import Bot

def run_bot(TOKEN):
    bot = Bot('?')
    cogs = [CrackWatch, HiBye, Sound]
    for cog in cogs:
        bot.add_cog(cog(bot))
    bot.run(TOKEN)

if __name__ == '__main__':
    from os import getenv
    run_bot(getenv('BOT_TOKEN'))