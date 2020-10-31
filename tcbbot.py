import discord, asyncio
from discord.ext.commands import Bot
from memelib.api import DankMemeClient

await myclient.meme(subreddit="dankmemes")

def get_token():
    import pickle
    with open("token.p",'rb') as fh:
        return pickle.load(fh)
    return None

client = Bot('?')
myclient = DankMemeClient(return_embed=True)

@client.command(name="hello")
async def hello(ctx):
    await ctx.send("Hello I'm the TCB Bot! I can't do anything yet, but I will soon.")

@client.command(name="memes")
async def memes(ctx):
    memb = await myclient.meme(subreddit="dankmemes")
    await ctx.send(embed=memb)

@client.event
async def on_message(message):
    # try:
    await client.process_commands(message)
    # except:
    #     pass

TOKEN = get_token()
print(TOKEN)
client.run(TOKEN)