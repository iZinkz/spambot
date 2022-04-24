import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import os

j=1
bot = commands.Bot(command_prefix="=", help_command=None)

@bot.event
async def on_ready():
    print("Josh ready to get bozo'd")

@bot.command(pass_context=True)
async def start(ctx):
    j=1
    while j == 1:
        await ctx.send("<@792122525135929355> is a fucking nerd", delete_after=0.000001)

@bot.command(pass_context=True)
async def stop(ctx):
    j=j+1        
        



bot.run("OTY3OTIwNTQ2NDM4MzI4MzUw.YmXUQQ.0DF14D7GEJdcKZgOEA92vmtJKqI")
