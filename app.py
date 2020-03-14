import os, sys
import discord
import asyncio
from discord.ext import commands
from datetime import * 
import runneron
import urllib 

TOKEN = os.environ([TOKEN])


Client = commands.Bot(command_prefix = '$')



@Client.command(pass_context = True)
async def whois(message, url):        
    fullname = "image.jpg"
    urllib.request.urlretrieve(url,fullname)         
    item = runneron.load(fullname)
    os.remove(fullname)
    await message.channel.send('Уверен это ' + item.get('kind') + ' на ' + item.get('prob') + '%' )



@Client.command(pass_context = True)
async def exit(message):
    print('!!CLOSED!!')
    raise SystemExit



@Client.command(pass_context = True)
async def clear(message, amount = 5):
    messages = []
    today = datetime.today()
    async for m in message.channel.history(limit = amount):
        delta = today - m.created_at
        if delta.days < 14:
            messages.append(m)
        else:
            pass
    await message.channel.delete_messages(messages)

        


@Client.event
async def on_ready():
    print('Logged in as')
    print(Client.user.name)
    print(Client.user.id)
    print('GOOD LUCK')


Client.run(TOKEN)