import os
from dotenv import load_dotenv
from discord.ext.commands import Bot
from cogs.hibye import *
from cogs.crackwatch import *

if os.path.exists('.env'):
    load_dotenv()

bot = Bot('?')
bot.add_cog(HiBye(bot))
bot.add_cog(CrackWatch(bot))

TOKEN = os.getenv('TOKEN')
bot.run(TOKEN)