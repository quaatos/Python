import discord
import random
import datetime

x = datetime.datetime.now()
DISCORD_TOKEN = "Your TOKEN here"

client = discord.Client()

@client.event
async def on_message(message):
    if message.author.bot: 
        return

    #user input
    if 'xd' in message.content.lower():
        await message.channel.send('Now tell me; what does "xd" mean?')

    if 'lol' in message.content.lower():
        await message.channel.send('what do you mean? i dont understand "lol"')

    if 'stupid' in message.content.lower():
        await message.channel.send('Be nice to eachother :=)')
    
    if 'ouwe' in message.content.lower():
        await message.channel.send('Jo ouwe')

    if 'hello' in message.content.lower():
        await message.channel.send('Hello! im Quaatos the almighty Discord Bot!')

    if 'fuck' in message.content.lower():
        await message.channel.send('I dont like swearing people')

    if 'who are you' in message.content.lower():
        await message.channel.send('Im Quaatos the almighty DiscordBot, Respect me or i will make you horny (what)')

    if 'haha' in message.content.lower():
        await message.channel.send('very funny')

    if 'wtf' in message.content.lower():
        await message.channel.send('Did you just said; wtf?')

    if 'i dont know' in message.content.lower():
        await message.channel.send('dumbass')

    if 'shit' in message.content.lower():
        await message.channel.send('did you just said shit?')

    if 'lmao' in message.content.lower():
        await message.channel.send('did you just said: Laugh My Ass Of?')

    if 'lmfao' in message.content.lower():
        await message.channel.send('you just said: Laugh My F*cking Ass Off')

    if 'gn' in message.content.lower():
        await message.channel.send('Good night Bro/Sis')

    if 'gm' in message.content.lower():
        await message.channel.send('Good morning Bro/Sis')

    if '!help' in message.content.lower():
        await message.channel.send ('Hello! thanks for asking my help! i got some features you will love! Try this: !fact, !date, !meme, gm, gn')

    if 'sus' in message.content.lower():
        await message.channel.send(file=discord.File('sus.gif'))

    if 'omg' in message.content.lower():
        await message.channel.send(file=discord.File('OMG.jpg'))
        
    #ASK QUAATOS
    if '!date' in message.content.lower():
        await message.channel.send(x)

    if '!fact' in message.content.lower():
        await message.channel.send('The tallest tree on planet earth has a size of: 115 meters, 377 feat')
    
    #memes
    if '!meme' in message.content.lower():
        await message.channel.send(file=discord.File(random.choice(('xxl.jpg', '763.jpg', 'woman.jpg', 'mom.jpg', 'gru.jpg', 'blessyou.jpg', 'water.jpg',
        'fadkid.jpg', 'shrek.jpg', 'space.jpg', '3AM.jpg', ''))))

client.run(DISCORD_TOKEN)



# last updated: 14-11-2021 / 14:16 
# Europe time zone
