import discord
import random
import datetime
TOKEN = "TOKEN"

dateTime = datetime.datetime.now()

facts = [
    'Plutonium is radioactive',
    '',
    'tungsten is the thoughest metal known on earth',
    '',
]

client = discord.Client()

@client.event
async def on_message(message):
    if message.author.bot: #bot won't respond to their own message
        return

    if '!help' is message.content.lower():
        await message.channel.send('porno')
        
    if '!fact' is message.content.lower():
        
 
 

client.run(TOKEN)


# ------ IDEAS ------- #
# let the script read a text file and take a random fact out of it
#