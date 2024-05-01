import discord
from discord.ext import commands
from config import TOKEN
from config import PREFIX

bot = commands.Bot(command_prefix=PREFIX, intents=discord.Intents.all())

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="!help"))

bot.run(TOKEN)