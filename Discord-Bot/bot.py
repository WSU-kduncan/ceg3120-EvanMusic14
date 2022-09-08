import os

import discord
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    guild = discord.utils.get(client.guilds, name=GUILD)

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    interstellar_quotes = [
        'We used to look up at the sky and wonder at our place in the stars. Now we just look down, and worry about our place in the dirt.',
        'Do not go gentle into that good night; Old age should burn and rave at close of day. Rage, rage against the dying of the light.',
        'Mankind was born on Earth. It was never meant to die here.',
        'Everybody good? Plenty of slaves for my robot colony?',
        "This world's a treasure, Don; but it's been telling us to leave for a while now.",
        "Love is the one thing we're capable of perceiving that transcends time and space.",
        "I'm not afraid of death. I'm an old physicist - I'm afraid of time.",
        'Popcorn at a ball game is unnatural. I want a hot dog.'
    ]

    interstellar_images = [
        'inter1.jpeg', 'inter2.jpeg', 'inter3.jpeg', 'inter4.jpeg', 'inter5.jpeg', 'inter6.jpeg', 'inter7.jpeg', 'inter8.jpeg'
    ]

    if message.content == '!tars':
        response = random.choice(interstellar_quotes)
        await message.channel.send(response)

    if message.content == '!case':
        picture = random.choice(interstellar_images)
        await message.channel.send(file=discord.File('./Images/' + picture))

client.run(TOKEN)