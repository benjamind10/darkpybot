import os
from dotenv import load_dotenv
import discord
from discord.ext import commands 

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!',intents=intents)

@bot.event
async def on_ready():
    print("The bot is ready!")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

bot.run(DISCORD_TOKEN)