import os
import asyncio
import time
import random
import datetime
import discord
from discord.ext import commands, tasks
from itertools import cycle
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
status = cycle(['helium prices rise', 'the sunset on Daymar','a Ninetails Lockdown', 'Ruffels sleep', 'YY_McFly fly', 'The Morrow tour'])
client = commands.Bot(command_prefix = "$")
bank_balance = 4534546
UEC = "{:,.2f}".format(bank_balance)


 
    


@client.event
async def on_ready():
    change_status.start()
    send_greeting.start()
    print("Maj. Torque Imbalance is standing by.")
  
   
   
    
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hello {member.name}, welcome to the Space Bastards! You probably saw one of our finely crafted advertisments. If you you have any questions feel free to ask Varian_Halai. Welcome, and happy plundering!'
    )
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if "why" in message.content.lower() and "bank" in message.content.lower():
        await message.channel.send("The guild bank is a way for us to experiment with payouts and give us a communal goal in the absence of guild mechanics.")
    await client.process_commands(message)

@client.command()
async def bank(ctx):
    await ctx.send(f'Bank balance is currently {UEC} aUEC')

@client.command()
async def deposit(ctx, amount):
    result = int(amount) + bank_balance
    f_amount = "{:,.2f}".format(int(amount))
    final = "{:,.2f}".format(result)
    await ctx.send(f'{ctx.message.author.nick} deposited {f_amount} in the bank! Bank balance is currently {final} aUEC')
@client.command()
async def set_balance(ctx, amount):
    bank_balance = int(amount)
   
    final = "{:,.2f}".format(bank_balance)
    await ctx.send(f' Bank balance is now {final} aUEC')
@tasks.loop(seconds=45)
async def change_status():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=next(status)))
@tasks.loop(seconds=55)
async def send_greeting():
    time = datetime.datetime.today()
    if time.hour == 10 and time.minute == 00:
            
        channel = await discord.utils.get(client.guilds[0].channels, name='space-general').send(f'Have a good {datetime.datetime.now().strftime("%A")}, you beautiful bastards!')

client.run(TOKEN)