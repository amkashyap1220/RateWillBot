import os
import time
import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_message(message):
    if message.author.name == 'Brother Man Will':
        if len(message.attachments) > 0:
            rating = random.randrange(1, 10)
            if rating <= 3:
                toSend = 'Hmmmm... not sure if this is the right audience. Rating: ' + str(rating)
            elif rating <= 6:
                toSend = 'Normally your memes are on the ends of the spectrum but this is quite average... Rating: ' + str(rating)
            else:
                toSend = 'Will, you really outdid yourself with this one! Rating: ' + str(rating)
            await message.channel.send(toSend)

@client.event
async def on_ready():
    print("I'm in")

client.run(TOKEN)