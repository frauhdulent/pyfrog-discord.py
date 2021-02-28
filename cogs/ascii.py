import discord
import pyfiglet
import sys
sys.dont_write_bytecode = True
from pyfiglet import Figlet
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from discord.ext.commands import Context
from discord.ext.commands import has_permissions, CheckFailure


class ASCII(commands.Cog):
    def __init__(self, client):
        self.client = client

    #@commands.command(invoke_without_command=True)
    #async def asciihelp(self, ctx):
        #em = discord.Embed(title = "Ascii Text:", description = "Interested in converting your boring messages into ascii style? gotchu.", color = 0x20ff00)
        #em.add_field(name = "Ascii Commands:", value = "**ascii, ascii-graffiti, ascii-3d**")    
        #em.set_footer(text=f"eg;- fr!ascii <your message>, fr!ascii_3d <your message>")

        #await ctx.send(embed = em)
    
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ascii(self, ctx, *, msg):
        ascii_banner = pyfiglet.figlet_format(msg)
        await ctx.send(f"```{ascii_banner}```")
    
    @ascii.error
    async def ascii_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f'{(ctx.message.author.mention)} Hey can you slow down just a bit? ``5 Seconds``', delete_after=7)
    
    @commands.command(aliases=['ascii-graffiti'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ascii_graffiti(self, ctx, *, msg):
        f = Figlet(font='graffiti')
        output = f.renderText(msg)
        await ctx.send(f"```{output}```")
    
    @ascii_graffiti.error
    async def graffiti_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f'{(ctx.message.author.mention)} Hey can you slow down just a bit? ``5 Seconds``', delete_after=7)
    
    #@commands.command(aliases=['ascii-3d'])
    #@commands.cooldown(1, 5, commands.BucketType.user)
    #async def ascii_3d(self, ctx, *, msg):
        #f = Figlet(font='3d')
        #output = f.renderText(msg)
        #await ctx.send(f"```{output}```")
    
    #@ascii_3d.error
    #async def ascii3d_error(self, ctx, error):
        #if isinstance(error, commands.CommandOnCooldown):
            #await ctx.send(f'{(ctx.message.author.mention)} Hey can you slow down just a bit? ``5 Seconds``', delete_after=7)

def setup(client):
    client.add_cog(ASCII(client))
