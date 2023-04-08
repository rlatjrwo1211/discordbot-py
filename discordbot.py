from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
load_dotenv()

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == f'{PREFIX}call':
        await message.channel.send("callback!")

    if message.content.startswith(f'{PREFIX}Hi'):
        await message.channel.send('Hello!')


try:
    client.run(MTA5NDI2MDk0MDA4Nzc2NzE5MA.GCp1GL.0kagHkQ5EanlJBPwxHJjmX4CrlgS1vtcqQOwXA)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
