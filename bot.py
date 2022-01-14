#import important libraries
import discord
import random

#special token unique for every bot/user
TOKEN = 'OTMxNTE5MTk3MTYxMzQ1MDU0.YeFm2w.8_oyoATkwL0ydf5Y3T0UZrrx5bg'

#adding the bot to the server
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#adding reponses
@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.channel.name)
    print(f'{username}:{user_message}')

    if message.author == client.user:
        return
    if message.channel.name == 'general':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'See you later {username}!')
            return

client.run(TOKEN)
