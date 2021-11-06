import discord
from discord import channel
from discord.ext import commands
from discord.flags import Intents

Intents=discord.Intents.default()
Intents.members=True

bot = commands.Bot(command_prefix='!',Intents=Intents)

@bot.event
async def on_ready():
   print(">> bot is online <<")

@bot.event
async def on_member_join(member):
   channel=bot.get_channel(870156844541296644)
   await channel.send(f'{member}join!')

@bot.event
async def on_member_remove(member):
   channel=bot.get_channel(870156844541296644)
   await channel.send(f'{member}leave!')

bot.run('')