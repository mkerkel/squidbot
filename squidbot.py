import discord
import logging
from discord.ext import commands
from pref import key
from pref import mute_role

# Error Logging
logger = logging.getLogger("discord")
logger.setLevel(logging.WARNING)
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
handler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s"))
logger.addHandler(handler)

bot = commands.Bot(command_prefix="!", description="ye")


@bot.event
async def on_ready():
    print("Logged in as " + bot.user.name)
    await bot.change_presence(game=discord.Game(name="!help for help"))


@bot.command(pass_context=True)
async def goss(ctx):
    """Returns a list of various user attributes"""
    member = ctx.message.author
    user_roles = ", ".join(str(role) for role in member.roles if str(role) != "@everyone")

    await bot.say("Name: {0} \n"
                  "Joined at: {0.joined_at}\n"
                  "Main role: {0.top_role}\n"
                  "Roles: {1}".format(member, user_roles))


# Muting users
@bot.command(pass_context=True)
@commands.has_permissions(manage_roles=True)
async def mute(ctx, user_name: discord.User):
    """!mute @user to mute the user"""
    for server_role in ctx.message.server.roles:
        if server_role.name == mute_role:
            mute_role_id = server_role
    await bot.add_roles(user_name, mute_role_id)
    await bot.say(str(user_name) + " has been muted!")


@mute.error
async def mute_error(error, ctx):
    print("Mute error: " + type(error).__name__)
    if isinstance(error, commands.BadArgument):
        await bot.say("Unknown user!")
    elif isinstance(error, commands.CheckFailure):
        await bot.say("You don't have permission to do that!")
    elif isinstance(error, commands.CommandInvokeError):
        await bot.say("I don't have permission to do that!")


# Unmute users
@bot.command(pass_context=True)
@commands.has_permissions(manage_roles=True)
async def unmute(ctx, user_name: discord.User):
    """!unmute @user to unmute the user"""
    for server_role in ctx.message.server.roles:
        if server_role.name == mute_role:
            mute_role_id = server_role
    await bot.remove_roles(user_name, mute_role_id)
    await bot.say(str(user_name) + " has been unmuted! Be good " + str(user_name) + "!")


@unmute.error
async def unmute_error(error, ctx):
    print("Unmute error: " + type(error).__name__)
    if isinstance(error, commands.BadArgument):
        await bot.say("Unknown user!")
    elif isinstance(error, commands.CheckFailure):
        await bot.say("You don't have permission to do that!")
    elif isinstance(error, commands.CommandInvokeError):
        await bot.say("I don't have permission to do that!")


# Kicking users
@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, user_name: discord.User):
    """!kick @user to kick user"""
    await bot.kick(user_name)
    await bot.say(str(user_name) + " has been kicked!")


@kick.error
async def kick_error(error, ctx):
    print("Kick error: " + type(error).__name__)
    if isinstance(error, commands.BadArgument):
        await bot.say("Unknown user!")
    elif isinstance(error, commands.CheckFailure):
        await bot.say("You don't have permission to do that!")
    elif isinstance(error, commands.CommandInvokeError):
        await bot.say("I don't have permission to do that!")


# Banning users
@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, user_name: discord.User):
    """!ban @user to ban user"""
    await bot.ban(user_name, 0)
    await bot.say(str(user_name) + " has been banned!")


@ban.error
async def ban_error(error, ctx):
    print("Ban error: " + type(error).__name__)
    if isinstance(error, commands.BadArgument):
        await bot.say("Unknown user!")
    elif isinstance(error, commands.CheckFailure):
        await bot.say("You don't have permission to do that!")
    elif isinstance(error, commands.CommandInvokeError):
        await bot.say("I don't have permission to do that!")


# Features to implement:
# Log server activity

bot.run(key)
