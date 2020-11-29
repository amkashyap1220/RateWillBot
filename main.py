import os
import random
import discord
# using env in order to hide my secret for the bot
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Creating the Client object, this is my connection to discord with the bot
client = discord.Client()

# This is the first event we are checking, if a message has been sent
@client.event
async def on_message(message):
    # Is this message from Will?
    if message.author.name == 'Brother Man Will':
        # Does this message have an attachment?
        if len(message.attachments) > 0:
            # Use fancy ML technique in order to decide what the meme should be rated.
            rating = random.randrange(1, 10)
            # Use conditionals to decided which message to send
            if rating <= 3:
                toSend = 'Hmmmm... not sure if this is the right audience. Rating: ' + str(rating)
            elif rating <= 6:
                toSend = 'Normally your memes are on the ends of the spectrum but this is quite average... Rating: ' + str(rating)
            else:
                toSend = 'Will, you really outdid yourself with this one! Rating: ' + str(rating)
            # Send the message in the channel
            await message.channel.send(toSend)

# This is the second event, it mainly serves as a visual guide to see if the bot made the connection or not.
@client.event
async def on_ready():
    # print a simple message
    print("I'm in")

# Run the bot
client.run(TOKEN)
