#!/usr/bin/env python3

# discord-py requirements
import asyncio
import discord
from discord.ext import commands
import asyncio

# for database
import sqlite3

# logger
import logging

# Other utilities
import os
import sys
from config import parser
import random
from datetime import datetime
from pytz import timezone

# List the extensions (modules) that should be loaded on startup.
startup = [
    "cogs.reminder", "cogs.memes", "cogs.helpers", "cogs.mod", "cogs.score",
    "cogs.quotes", "cogs.images"
]

bot = commands.Bot(command_prefix='?')

# Logging configuration
logger = logging.getLogger('discord')
logger.setLevel(logging.ERROR)
handler = logging.FileHandler(
    filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(
    logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


@bot.event
async def on_ready():
    print('Logged in as {0} ({1})'.format(bot.user.name, bot.user.id))


@bot.command()
@commands.has_role("Discord Moderator")
async def load(ctx, extension_name: str):
    '''
    Load a specific extension.
    '''
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await ctx.send("```{}: {}\n```".format(type(e).__name__, str(e)))

        return
    await ctx.send("{} loaded.".format(extension_name))


@bot.command()
@commands.has_role("Discord Moderator")
async def unload(ctx, extension_name: str):
    '''
    Unload a specific extension.
    '''
    bot.unload_extension(extension_name)
    await ctx.send("Unloaded {}.".format(extension_name))


@bot.command()
@commands.has_role("Discord Moderator")
async def restart(ctx):
    '''
    Restart the bot
    '''
    await ctx.send('https://streamable.com/dli1')
    python = sys.executable
    os.execl(python, python, *sys.argv)


@bot.command()
@commands.has_role("Discord Moderator")
async def sleep(ctx):
    '''
    Shut down the bot
    '''
    await ctx.send('Bye')
    await bot.logout()
    print('Bot shut down')


@bot.command()
async def update(ctx):
    '''
    Update the bot by pulling changes from the git repository
    '''
    await ctx.send('https://streamable.com/c7s2o')
    os.system('git pull')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content == "dammit marty":
        await message.channel.send(":c")
    if message.content == "worm":
        await message.channel.send(
            "walk without rhythm, and it won't attract the worm.")
    if message.content == "hey":
        await message.channel.send("whats going on?")
    if message.content == "this is so sad, marty play despacito":
        await message.channel.send("`Now playing:` https://www.youtube.com/watch?v=kJQP7kiw5Fk")
    await bot.process_commands(message)


@bot.command()
@commands.has_role("Discord Moderator")
async def backup(ctx):
    '''
    Send the current database file to the owner
    '''
    current_time = datetime.now(tz=timezone('America/New_York')).strftime('%Y%m%d-%H:%M')
    backup_filename = 'Martlet%s.db' % current_time
    await ctx.send(
        content='Here you go',
        file=discord.File(
            fp=bot.config.db_path,
            filename=backup_filename))

# Startup extensions
# If statement will only execute if we are running this file (i.e. won't run
# if it's imported)
if __name__ == "__main__":
    bot.config = parser.Parser()
    conn = sqlite3.connect(bot.config.db_path)
    c = conn.cursor()
    with open('./Martlet.schema') as fp:
        c.executescript(fp.read())
        conn.commit()
        conn.close()
    for extension in startup:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print('Failed to load extension {}\n{}: {}'.format(
                extension,
                type(e).__name__, e))
    bot.run(bot.config.discord_key)
