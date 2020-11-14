import os
from dotenv import load_dotenv
from discord.ext.commands import Bot
from cogs import *

if os.path.exists('.env'):
    load_dotenv()

bot = Bot('?')
cogs = [ Aternos, CrackWatch, HiBye, Sound]
for cog in cogs:
    bot.add_cog(cog(bot))

TOKEN = os.getenv('BOT_TOKEN')
bot.run(TOKEN)