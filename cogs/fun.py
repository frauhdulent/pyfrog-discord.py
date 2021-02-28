import discord
import sys, traceback
import random
import math
sys.dont_write_bytecode = True
from random import randint
from discord.ext import commands


class fun(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def coinflip(self, ctx):
        choices = ["Heads", "Tails", "The coin fell down, Try again."]
        rancoin = random.choice(choices)
        await ctx.send(rancoin)
    
    @commands.command(pass_context=True)
    async def howcool(self, ctx, member: discord.Member=None):
        value = randint(0, 100)
        if member == None:
            await ctx.send(f"you're this cool {value}%")
        if member != None:
            await ctx.send(f"{member.mention} you're this cool {value}%")
    
    @commands.command(aliases=['howlongpp', 'bigpp', 'smallpp'])
    async def pp(self, ctx, member: discord.Member=None):
        responses = [
            "8==D",
            "8===D",
            "8====D",
            "8=====D",
            "8======D",
            "8=======D",
            "8========D",
            "8=========D",
            "8==========D"
        ]
        if member == None:
            await ctx.send(f'**{random.choice(responses)}** This is how long your pp is!')
        if member != None:
            await ctx.send(f'**{random.choice(responses)}** This is how long {member.mention} pp is!')


def setup(client):
    client.add_cog(fun(client))
