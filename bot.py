import discord
import asyncio
import time

from stats import Stats
from clan import Clan,Time

token = open('token.txt',"r").read().strip()

RENAMETIME=1547524924
CDDUR = 2592000

client = discord.Client()

@client.event
async def on_read():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1
        await client.edit_message(tmp, 'You have {} messages.'.format(counter))

    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

    elif message.content.startswith('!available EST'):
        await client.send_message(message.channel,'Rename available at '+Time.available('EST')+' EST')
        
    elif message.content.startswith('!available PST'):
        await client.send_message(message.channel,'Rename available at '+Time.available('PST')+' PST')

    elif message.content.startswith('!available'):
        await client.send_message(message.channel,'Rename available at '+Time.available('UTC')+' UTC')

    elif message.content.startswith("cv"):
        await client.send_message(message.channel,'REEEEEEEEEE')

client.run(token)
