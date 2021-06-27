import discord
import math
import sys, traceback
sys.dont_write_bytecode = True
from discord.ext.commands import CommandNotFound
from discord.ext.commands import Context
from discord.ext.commands import has_permissions, CheckFailure
from discord import User
from discord.utils import get
from discord.ext import commands


class mod(commands.Cog):
    def __init__(self, client):
        self.client = client
    

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'{member} has been banned.')
    
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'{(ctx.message.author.mention)} Uhm you forgot to mention the user.')

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'User {member} has been kick')
    
    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'{(ctx.message.author.mention)} Uhm you forgot to mention the user.')
    
    
    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def purge(self, ctx, limit: int):
        await ctx.channel.purge(limit=limit)
        await ctx.send('Cleared by {}'.format(ctx.author.mention))
        await ctx.message.delete()

    @clean.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have administrator role.")

def setup(client):
    client.add_cog(mod(client))
    
