import discord
import logging
from discord.ext import commands

# Error Logging
logger = logging.getLogger('discord')
logger.setLevel(logging.WARNING)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

bot = commands.Bot(command_prefix='!', description='ye')


@bot.event
async def on_ready():
    print('Logged in as ' + bot.user.name)
    await bot.change_presence(game=discord.Game(name='!help for help'))


@bot.command()
async def hey():
    await bot.say('Sup')


@bot.command(pass_context=True)
async def goss(ctx):
    """Returns a list of various user attributes"""
    member = ctx.message.author
    user_roles = ''
    user_roles += ", ".join(str(role) for role in member.roles if str(role) != "@everyone")

    await bot.say('Name: {0} \n'
                  'Joined at: {0.joined_at}\n'
                  'Main role: {0.top_role}\n'
                  'Roles: {1}'.format(member, user_roles))


@bot.command(pass_context=True)
async def kick(ctx, content: discord.Message):
    if content is None:
        content = ctx.message.content

        await bot.say(content)

# Features to implement:
# Mute
# Kick
# Ban
# Log server activity

bot.run()