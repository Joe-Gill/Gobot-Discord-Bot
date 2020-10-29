import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!intro'):
        await message.channel.send('My name is Go-bot. Legendary Discord bot.')

tokenFile = open("src/.token.txt","r")
token = tokenFile.readline()
tokenFile.close()

client.run(token)
