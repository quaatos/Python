import discord
import random
import datetime
import string

TOKEN = "YOUR TOKEN"

dateTime = datetime.datetime.now()
MonthDay = dateTime.strftime("%d")
Month = dateTime.strftime("%B")
Year = dateTime.strftime("%Y")

#open file and take a random sentence
with open('facts.txt') as f:
    fact = f.readlines()

#open file and take random quote
with open('quotes.txt', encoding='utf-8') as f:
    quotes = f.readlines()

client = discord.Client()

@client.event
async def on_message(message):
    #bot status
    await client.change_presence(activity=discord.Game('!help'))

    if message.author.bot: #bot won't respond to their own message
        return

    if '!help' == message.content.lower():
        await message.channel.send('\n `!help` --- Print available commands\n `!fact` --- Print a random fact\n `!ryt` --- random youtube link\n `!rph` --- random pornhub link')
        await message.channel.send(' `!date` --- get the date of today\n `!source` --- my source code\n`!quote` --- random quote')

    if '!fact' == message.content.lower():
        await message.channel.send(random.choice(fact))

    if '!ryt' == message.content.lower():
        ran = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits + "-_", k = 11))
        await message.channel.send("https://youtu.be/watch?v=" + str(ran))

    if '!rph' == message.content.lower():
        ran = ''.join(random.choices(string.ascii_lowercase + string.digits, k = 13))
        await message.channel.send("https://pornhub.com/view_video.php?viewkey=ph" + str(ran))

    if '!date' == message.content.lower():
        await message.channel.send("date: " + '**' + Month + ' ' + MonthDay + ', ' + Year + '**')

    if '!quote' == message.content.lower():
        await message.channel.send(random.choice(quotes))

    if '!source' == message.content.lower():
        await message.channel.send("https://github.com/quaatos/Python/tree/main/slykaBot")

client.run(TOKEN)

# ------ IDEAS ------- #
#                      #
#                      #

#developed with love by quaatos and skaffa
#https://github.com/skaffa
#https://github.com/quaatos
