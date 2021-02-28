import discord
import sys
sys.dont_write_bytecode = True
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        em = discord.Embed(title = "Commands:", description = "For more info regarding specific commands, ``fr!help <command>``", color = 0x20ff00)
        em.add_field(name = "Mathematical functions:", value = "**√** Sqrt, **+** Addition, **-** Subtract, ***** Multiply, **/** Division, **²** Square")   
        em.set_footer(text=f"Don't get confused by the Symbols, All you have to do is fr!help subtract, fr!help addition")
        await ctx.send(embed = em)
    
    @help.command()
    async def sqrt(self, ctx):
        em = discord.Embed(title = "Sqrt:", description = "Returns the **square root** of any number.", color = 0x20ff00)
        em.add_field(name = "**Sqrt**", value = "fr!sqrt <number>")
        em.set_footer(text=f"eg:- fr!sqrt 9")
        await ctx.send(embed = em)
    
    @help.command(aliases=['add'])
    async def addition(self, ctx):
        em = discord.Embed(title = "Addition:", description = "Returns the **sum** of two numbers.", color = 0x20ff00)
        em.add_field(name = "**Addition**", value = "fr!add <number> <number>")
        em.set_footer(text=f"eg:- fr!add 2 2")
        await ctx.send(embed = em)
    
    @help.command(aliases=['sub'])
    async def subtract(self, ctx):
        em = discord.Embed(title = "Subtract:", description = "Returns the **difference** of two numbers.", color = 0x20ff00)
        em.add_field(name = "**Subtract**", value = "fr!subtract <number> <number>")
        em.set_footer(text=f"eg:- fr!subtract 2 2")
        await ctx.send(embed = em)
    
    @help.command(aliases=['multiplication'])
    async def multiply(self, ctx):
        em = discord.Embed(title = "Multiply:", description = "Returns the **product** of two numbers.", color = 0x20ff00)
        em.add_field(name = "**Multiply**", value = "fr!multiply <number> <number>")
        em.set_footer(text=f"eg:- fr!multiply 9 8")
        await ctx.send(embed = em)
    
    @help.command(aliases=['division'])
    async def divide(self, ctx):
        em = discord.Embed(title = "Division:", description = "Returns the **product** of a number divided by another number.", color = 0x20ff00)
        em.add_field(name = "**Division**", value = "fr!divide <number> <number>")
        em.set_footer(text=f"eg:- fr!divide 9 8")
        await ctx.send(embed = em)

    @help.command()
    async def square(self, ctx):
        em = discord.Embed(title = "Square:", description = "Squares a given number.", color = 0x20ff00)
        em.add_field(name = "**Square**", value = ">Square <number> <number>")
        em.set_footer(text=f"eg:- fr!square 10 8")
        await ctx.send(embed = em)
    
    @help.command(aliases=['ascii'])
    async def asciihelp(self, ctx):
        em = discord.Embed(title = "Ascii Text:", description = "Interested in converting your boring messages into ascii style? gotchu.", color = 0x20ff00)
        em.add_field(name = "Ascii Commands:", value = "**ascii, ascii-graffiti, ascii-3d**")    
        em.set_footer(text=f"eg;- fr!ascii <your message>, fr!ascii_3d <your message>")
        await ctx.send(embed = em)


def setup(client):
    client.add_cog(Help(client))
