import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!',description='ye')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)

@bot.command()
async def hey():
    await bot.say('Sup')

#bot.run('')
