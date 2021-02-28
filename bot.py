import discord
import math
import random
import asyncio
import json
import io
import aiohttp
import requests
import os
import urllib.request
import datetime, time
import pyfiglet
import sys
sys.dont_write_bytecode = True
from pyfiglet import Figlet
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from discord.ext.commands import Context
from discord.ext.commands import has_permissions, CheckFailure
from io import BytesIO

TOKEN = " your token. "
custom_prefixes = {}
get_prefix = ['fr!', 'frog']

client = commands.Bot(command_prefix = get_prefix)
client.remove_command("help")

activity_status = "Interstellar frog at your service, fr!help"

cogs = ['cogs.mod', 'cogs.fun', 'cogs.math', 'cogs.owner', 'cogs.random', 'cogs.ascii', 'cogs.help']

@client.event
async def on_ready():
    activity_string = '{} servers, fr!help'.format(len(client.guilds))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=activity_string))

    print("Bot Online!")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))

    for cog in cogs:
        client.load_extension(cog)
    return

@client.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            em = discord.Embed(title = None, description = None, color = 0x20ff00)
            em.add_field(name = "Info:", value = "Heyo thanks for adding me to your server i really mean it, ``fr!help`` for help")
            em.add_field(name = "Developer:", value = "Check out the developer's github page ---> **https://github.com/clancyy**")
            await channel.send(f'AYO WHO SUMMONED ME? jk', embed = em)
        break

@client.command(aliases=['latency'])
async def ping(ctx):
    await ctx.send(f'**Pong! ``{round(client.latency * 1000)}ms``**')

#@client.command()
#@has_permissions(ban_members=True)
#async def unban(ctx, userid:int):
        #user = await client.fetch_user(userid)
        #await ctx.guild.unban(user)
        #await ctx.send(f'{userid} has been unbanned.')

start_time = time.time()

@client.command(pass_context=True)
async def uptime(ctx):
    current_time = time.time()
    difference = int(round(current_time - start_time))
    text = str(datetime.timedelta(seconds=difference))
    await ctx.send("**Current uptime: **" + text)


client.run(TOKEN)
