import os
from dotenv import load_dotenv
from discord.ext.commands import Bot
from cogs.hibye import *
from cogs.crackwatch import *
from cogs.aternos import *

if os.path.exists('.env'):
    load_dotenv()

bot = Bot('?')
cogs = [HiBye, CrackWatch, Aternos]
for cog in cogs:
    bot.add_cog(cog(bot))

TOKEN = os.getenv('TOKEN')
bot.run(TOKEN)