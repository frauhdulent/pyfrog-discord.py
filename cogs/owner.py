import discord
import asyncio
import sys
sys.dont_write_bytecode = True
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure


class owner(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    @commands.is_owner()
    async def shutdown(self, ctx):
        msg = await ctx.send(f"Commencing shutdown in T-minus 10 seconds...")
        await asyncio.sleep(1)
        await msg.edit(content="Commencing shutdown in T-minus 9 seconds...")
        await asyncio.sleep(1)
        await msg.edit(content="Commencing shutdown in T-minus 8 seconds...")
        await asyncio.sleep(1)
        await msg.edit(content="Commencing shutdown in T-minus 7 seconds...")
        await asyncio.sleep(1)
        await msg.edit(content="Commencing shutdown in T-minus 6 seconds...")
        await asyncio.sleep(1)
        await msg.edit(content="Commencing shutdown in T-minus 5 seconds...")
        await asyncio.sleep(1)
        await msg.edit(content="Commencing shutdown in T-minus 4 seconds...")
        await asyncio.sleep(1)
        await msg.edit(content="Commencing shutdown in T-minus 3 seconds...")
        await asyncio.sleep(1)
        await msg.edit(content="Commencing shutdown in T-minus 2 seconds...")
        await asyncio.sleep(1)
        await msg.edit(content="Commencing shutdown in T-minus 1 seconds...", delete_after=0.5)
        await asyncio.sleep(1)
        await ctx.bot.logout()
    
    @shutdown.error
    async def shutdown_error(self, ctx, error):
        if isinstance(error, commands.NotOwner):
            await ctx.send(f'{(ctx.message.author.mention)} You do not own this bot.')
    
    @commands.command()
    @commands.is_owner()
    async def history(self, ctx, limit: int = 100):
            messages = await ctx.channel.history(limit=limit).flatten()
            with open("channel_messages.txt", "a+", encoding="utf-8") as f:
                print(*messages, sep="\n\n", file=f)
                await ctx.send(f'You have successfully exported a save for this chat.')
    
    @history.error
    async def history_error(self, ctx, error):
        if isinstance(error, commands.NotOwner):
            await ctx.send(f'{(ctx.message.author.mention)} You do not own this bot.')
    
    @commands.command(name="say", pass_context=True, aliases=["announce"])
    @commands.is_owner()
    async def say(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @say.error
    async def say_error(self, ctx, error):
        if isinstance(error, commands.NotOwner):
            await ctx.send(f'{(ctx.message.author.mention)} You do not own this bot.')

def setup(client):
    client.add_cog(owner(client))
