import discord,aiomysql,aiohttp,async_timeout,asyncio,traceback,sys,keys
import datetime
from datetime import date
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import sys
import dbl
import logging

#Makes the traceback 1 line.
sys.tracebacklimit = 0

# Below cogs represents our folder our cogs are in. Following is the file name. So 'meme.py' in cogs, would be cogs.meme
# Think of it like a dot path import
initial_extensions = ['cogs.gear','cogs.gearhelp','cogs.errors']
# Enable this if you're a developer with a dbl key
#initial_extensions = ['cogs.gear','cogs.dbl_api','cogs.gearhelp','cogs.errors']

bot = commands.Bot(command_prefix='!', description='gearBot')

# Here we load our extensions(cogs) listed above in [initial_extensions].
if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()


#Displays the bots tags,ID and the amount of servers the bot is connected to in terminal
@bot.event
async def on_ready():
    count = 0
    for guild in bot.guilds:
        count = count + 1
        #print(guild.name)
    print("\n".join(
        ["#" * 25, "Name:{0.name}#{0.discriminator}".format(bot.user), "ID : {}".format(bot.user.id), "Servers: {}".format(count), "#" * 25]))




#Silences the error commands if someone using a command this bot doesn't support with it's prefex.
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error



#Pass your bots api key here
bot.run(keys.gearBot)