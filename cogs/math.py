import discord
import math
import random
import sys
sys.dont_write_bytecode = True
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure


class maths(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def sqrt(self, ctx, a:float):
        await ctx.send(f"**√ Of {(round(a))} Is: {math.sqrt(a)}**")

    @sqrt.error
    async def sqrt_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(f"{(ctx.message.author.mention)} That isn't an integer.")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"{(ctx.message.author.mention)} Missing Integer.")
    
    @commands.command()
    async def isclose(self, ctx, a:float,b:float):
        await ctx.send(math.isclose(a, b))
    
    @isclose.error
    async def isclose_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(f"{(ctx.message.author.mention)} That isn't an integer.")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"{(ctx.message.author.mention)} Missing Integer.")
    
    @commands.command()
    async def isfinite(self, ctx, num:float):
        await ctx.send(math.isfinite(num))
    
    @isfinite.error
    async def isfinite_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(f"{(ctx.message.author.mention)} That isn't an integer.")
    
    @commands.command()
    async def pi(self, ctx):
        await ctx.send(f"{math.pi} The value of π")
    
    @pi.error
    async def pi_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(f"{(ctx.message.author.mention)} That isn't an integer.")

    @commands.command()
    async def cos(self, ctx, num:float):
        await ctx.send(math.sin(num))
    
    @cos.error
    async def cos_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(f"{(ctx.message.author.mention)} That isn't an integer.")
    
    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def add(self, ctx,a:float,b:float):
        await ctx.send(a+b)
        await ctx.send(f"Rounded to: {(round(a+b))}")
    @add.error
    async def add_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f'{(ctx.message.author.mention)} Hey can you slow down just a bit? ``2 Seconds``', delete_after=4)
        if isinstance(error, commands.BadArgument):
            await ctx.send(f"{(ctx.message.author.mention)} That isn't an integer.")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"{(ctx.message.author.mention)} Missing Integer.")
    
    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def subtract(self, ctx,a:float,b:float):
        await ctx.send(a-b)
        await ctx.send(f"Rounded to: {(round(a-b))}")
    @subtract.error
    async def subtract_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f'{(ctx.message.author.mention)} Hey can you slow down just a bit? ``2 Seconds``', delete_after=4)
        if isinstance(error, commands.BadArgument):
            await ctx.send(f"{(ctx.message.author.mention)} That isn't an integer.")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"{(ctx.message.author.mention)} Missing Integer.")
    
    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def multiply(self, ctx,a:int,b:int):
        await ctx.send(a*b)
        await ctx.send(f"Rounded to: {(round(a*b))}")
    @multiply.error
    async def multiply_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f'{(ctx.message.author.mention)} Hey can you slow down just a bit? ``2 Seconds``', delete_after=4)
        if isinstance(error, commands.BadArgument):
            await ctx.send(f"{(ctx.message.author.mention)} That isn't an integer.")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"{(ctx.message.author.mention)} Missing Integer.")
    
    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def divide(self, ctx,a:float,b:float):
        await ctx.send(a/b)
        await ctx.send(f"Rounded to: {(round(a/b))}")
    @divide.error
    async def divide_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f'{(ctx.message.author.mention)} Hey can you slow down just a bit? ``2 Seconds``', delete_after=4)
        if isinstance(error, commands.BadArgument):
            await ctx.send(f"{(ctx.message.author.mention)} That isn't an integer.")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"{(ctx.message.author.mention)} Missing Integer.")
    
    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def square(self, ctx,a:float,b:float):
        await ctx.send(a**b)
        await ctx.send(f"Rounded to: {(round(a**b))}")

    @square.error
    async def square_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f'{(ctx.message.author.mention)} Hey can you slow down just a bit? ``2 Seconds``', delete_after=4)
        if isinstance(error, commands.BadArgument):
            await ctx.send(f"{(ctx.message.author.mention)} That isn't an integer.")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"{(ctx.message.author.mention)} Missing Integer.")

def setup(client):
    client.add_cog(maths(client))
