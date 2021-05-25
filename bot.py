import os
import asyncio
import time
import random
import datetime
import discord
from discord.ext import commands, tasks
from itertools import cycle


TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
status = cycle(['fireworks at Everus', 'the sunset on Daymar','a Ninetails Lockdown', 'Ruffels sleep', 'old combat footage', 'The Morrow tour', 'The Bengal flyby'])
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
    formatted_amount = "{:,.2f}".format(int(amount))
    final = "{:,.2f}".format(result)
    await ctx.send(f'{ctx.message.author.nick} deposited {formatted_amount} in the bank! Bank balance is currently {final} aUEC')
@client.command()
async def set_balance(ctx, amount):
    bank_balance = int(amount)
   
    final = "{:,.2f}".format(bank_balance)
    await ctx.send(f' Bank balance is now {final} aUEC')
@tasks.loop(seconds=180)
async def change_status():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=next(status)))
@tasks.loop(hours=1)
async def send_greeting():
    day = datetime.datetime.now().strftime("%A")
    time = datetime.datetime.today()
    if day == "Tuesday":
        if time.hour == 15:  
            await discord.utils.get(client.guilds[0].channels, name='space-general').send(f"{day} is a good day for trainin'! Grab a battle buddy and get some time in Arena Commander!")

client.run(TOKEN)