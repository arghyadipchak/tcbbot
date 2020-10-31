import discord, asyncio
from discord.ext.commands import Bot

def get_token():
    import pickle
    with open("token.p",'rb') as fh:
        return pickle.load(fh)
    return None

client = Bot('?')

@client.command(name="hello")
async def hello(ctx):
    await ctx.send("Hello I'm the TCB Bot! I can't do anything yet, but I will soon.")

@client.event
async def on_message(message):
    # try:
    await client.process_commands(message)
    # except:
    #     pass

TOKEN = get_token()
print(TOKEN)
client.run(TOKEN)