import discord,aiomysql,aiohttp,async_timeout,asyncio,traceback,sys
from cogs.modules import db_sessions, urlChecker, logger
import datetime
from datetime import date
from discord.ext import commands
from discord.ext.commands import CommandNotFound

class gearhelp_Cog(commands.Cog, name="Owner Commands"):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='gearhelp')
    async def gearhelp(self, ctx):
        """!gearhelp for a nicer view of the help commands."""
        embed = discord.Embed(colour=discord.Colour(0xa9219b))
        #embed.set_image(url="https://cdn.discordapp.com/embed/avatars/0.png")
        embed.set_thumbnail(url="https://n0tj.com/g_center.png")
        embed.set_author(name="Join the gearBot discord", url="https://discord.gg/Eb6PFUF", icon_url="https://n0tj.com/g_center.png")
        embed.set_footer(text="Message jay#8008 with any bugs or concerns.", icon_url="https://n0tj.com/buddha.jpeg")
        embed.add_field(name="**Updating your gear screenshot**", value="**!gear <link>**")
        embed.add_field(name="**Looking up someone or your own gear**", value="**!gear <@user>**")
        #embed.add_field(name="**Get gearBot for your server!**", value="**!gear <@user>**")


        await ctx.send(embed=embed)

#Adding this as a cog
def setup(bot):
    bot.add_cog(gearhelp_Cog(bot))