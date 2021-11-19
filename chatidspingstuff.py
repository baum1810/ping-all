
token = "YOUTOKEN"

from discord.ext import commands
from discord.utils import get
import discord
import requests
import asyncio
import json


loop = asyncio.get_event_loop()

def cls():
    system('cls')

prefix = "!"

bot = discord.Client()
bot = commands.Bot(description='test', command_prefix=prefix, self_bot=True)
bot.remove_command('help')

def my_function(x):
  return list(dict.fromkeys(x))

@bot.event
async def on_ready():
    print("online")
    
@bot.command()    
async def test(ctx):
    await ctx.message.delete()
    channelid = ctx.channel.id
    headers = {
        'authorization' : token
    }
    listt = []
    listtt = []
    r = requests.get(f"https://discord.com/api/v8/channels/{channelid}/messages", headers=headers)
    jsonn = json.loads(r.text)
    for value in jsonn:
        
        test = value['author']
        test2 = test['id']
        listt += [test2]
        #await ctx.send(f"<@{test2}>")
        
    test3 =  list(dict.fromkeys((listt)))    
    for x in test3:
        deinemumi = f"<@{x}>"
        listtt += [deinemumi]

    await ctx.send(listtt)
    await ctx.message.delete()
   



bot.run(token, bot=False, reconnect=True)