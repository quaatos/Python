import discord
import random
import datetime
import string
TOKEN = "DISCORD TOKEN"

dateTime = datetime.datetime.now()
MonthDay = dateTime.strftime("%d")
Month = dateTime.strftime("%B")

with open('facts.txt') as f:
    lines = f.readlines()

client = discord.Client()

@client.event
async def on_message(message):
    if message.author.bot: #bot won't respond to their own message
        return

    if '!help' == message.content.lower():
        await message.channel.send('\n `!help` --- Print available commands\n `!fact` --- Print a random fact\n `!ryt` --- random youtube link\n `!rph` --- random pornhub link')
        await message.channel.send(' `!date` --- get the date of today')

    if '!fact' == message.content.lower():
        await message.channel.send(random.choice(lines))

    if '!ryt' == message.content.lower():
        ran = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits + "-_", k = 11))
        await message.channel.send("https://youtu.be/watch?v=" + str(ran))

    if '!rph' == message.content.lower():
        ran = ''.join(random.choices(string.ascii_lowercase + string.digits, k = 13))
        await message.channel.send("https://pornhub.com/view_video.php?viewkey=ph" + str(ran))

    if '!time' == message.content.lower():
        await message.channel.send("date: " + Month + ' ' + MonthDay)
    
    
client.run(TOKEN)

# ------ IDEAS ------- #
# 
#
