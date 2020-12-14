import traceback
import sys
from discord.ext import commands
import discord
import asyncio


class errors_Cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(colour=discord.Colour(0xa9219b))

            #embed.set_image(url="https://cdn.discordapp.com/embed/avatars/0.png")
            embed.set_thumbnail(url="https://n0tj.com/g_center.png")
            embed.set_author(name="Join the gearBot discord", url="https://discord.gg/jZAJ7Yy", icon_url="https://n0tj.com/g_center.png")
            embed.set_footer(text="Message jay#8008 with any bugs or concerns.", icon_url="https://n0tj.com/buddha.jpeg")
            embed.add_field(name="**Updating your gear screenshot**", value="**!gear <link>**")
            embed.add_field(name="**Looking up someone or your own gear**", value="**!gear <@user>**")


            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(errors_Cog(bot))
