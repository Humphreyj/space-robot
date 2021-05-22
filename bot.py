import os

import discord
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()
'''
A client is an object that represents a connection to Discord. A client handles events, tracks state and interacts with Discord APIs
'''

@client.event
async def on_ready():
    '''
Here we have created a client and implemented its on_ready() handler which will be called once the client is ready for further action.
'''
    # for guild in client.guilds:
    #     if guild.name == GUILD:
    #         break

@client.event
async def on_ready():
    print(f'{client.user.name} has connected!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hello {member.name}, welcome to the Space Bastards! You probably saw one of our finely crafted advertisments. If you you have any questions feel free to ask Varian_Halai. Welcome, and happy plundering!'
    )


client.run(TOKEN)