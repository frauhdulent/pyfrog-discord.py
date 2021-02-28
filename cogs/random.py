import io
import os
import discord
import requests
import sys
sys.dont_write_bytecode = True
from io import BytesIO
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure


class random(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def person(self, ctx):
        image_url = "https://thispersondoesnotexist.com/image"
        img_data = requests.get(image_url).content
        with open('person.jpg', 'wb') as handler:
            handler.write(img_data)
        await ctx.send(file = discord.File("person.jpg"))
        await ctx.send("This person doesn't exist. https://thispersondoesnotexist.com")
        os.remove("person.jpg")
    
    @person.error
    async def person_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f'{(ctx.message.author.mention)} Hey can you slow down just a bit? ``10 Seconds``', delete_after=7)
    
    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def art(self, ctx):
        image_url = "https://thisartworkdoesnotexist.com/"
        img_data = requests.get(image_url).content
        with open('art2.jpg', 'wb') as handler:
            handler.write(img_data)
        await ctx.send(file = discord.File("art2.jpg"))
        await asyncio.sleep(1)
        os.remove("art2.jpg")
        await ctx.send("This art doesn't exist.")

    @art.error
    async def art_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f'{(ctx.message.author.mention)} Hey can you slow down just a bit? ``10 Seconds``', delete_after=7)
    
    @commands.command()
    async def root(ctx):
        responses = [
            "error: wrong password!",
            "error: you aren't a root user.",
            "error: have you tried restarting your computer?",
            "error: sorry i can't help you today maybe use the Ubuntu Software Center?",
            "error: sorry im not connected to the internet."
            "error: stop wasting my time."
        ]
        
        message = await ctx.send("root" + ctx.message.author.mention + ":~$")
        await asyncio.sleep(3)
        await message.edit(content = f'{random.choice(responses)}')

def setup(client):
    client.add_cog(random(client))
