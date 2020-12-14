import discord,aiomysql,aiohttp,async_timeout,asyncio,traceback,sys
from cogs.modules import db_sessions, urlChecker, logger
import datetime
from datetime import date
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import keys
import aiohttp
import json
import random
import time



#Add attachment grabbing https://stackoverflow.com/questions/59181208/discord-py-bot-take-file-as-argument-to-command




class gear_Cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #Not in use now, might be useful later.
    def stripID(discord_id):
            sanitize_user_id_v1 = str(discord_id)
            sanitize_user_id_v2 = sanitize_user_id_v1.replace("(", "")
            sanitize_user_id_v3 = sanitize_user_id_v2.replace(",)", "")
            return(sanitize_user_id_v3)


    @commands.command(name='gear')
    async def gear(self, ctx, args):
        """First update your gear with !gear <link> then query your gear and other players with !gear <@user>"""
        user = ctx.author
        str_user = str(user)

        #Temporary fix with this len nonsense, look into fixing this it determiens if someone passed a mention @Dec-6-2020
        if len(args) == 21 or len(args) == 22:
        #if args.isdigit() or len(args) == 21:
            #Utlity for gettings mentions ID, tag, etc.
            name = ctx.message.mentions[0].name
            discriminator = ctx.message.mentions[0].discriminator
            tag = ('{}#{}'.format(name,discriminator))
            mentionID = str(ctx.message.mentions[0].id)
            mentionAvatar = str(ctx.message.mentions[0].avatar_url)
            getTag = str(tag)


            verifyUser = (await db_sessions.dyno_check_user(mentionID))
            if mentionID == verifyUser:
                #Check to see weather they can have a direct link or not and then chooses the format based on that.
                some_list = [await db_sessions.dyno_get_link(mentionID)]
                extensions = ['.jpg', '.png', '.PNG', '.JPG', '.jpeg', '.JPEG', '.gif', '.GIF']
                flag = 0
                for s in some_list:
                    for item in extensions:
                        if item in s:
                            flag = 1
                if flag == 0:
                        #Legacy layout
                        #TODO: Write something here that will take the link provided and return a direct link, that will be updated in the database server side
                        print(("User mention: {}").format(str(ctx.author.mention)))
                        await ctx.send("Legacy layout, use a direct link next time. \n{}'s gear: {}".format(args, await db_sessions.dyno_get_link(mentionID)))
                        #Logging
                        await logger.bigLog.log_5(ctx,str_user,str(getTag))
                else:
                    #Fancy frame for displaying user screenshot
                    bio = await db_sessions.dyno_get_bio(mentionID)
                    embed = discord.Embed(colour=discord.Colour(0xa9219b))
                    embed.set_image(url=await db_sessions.dyno_get_link(mentionID))
                    embed.set_thumbnail(url=mentionAvatar)
                    embed.add_field(name="A bio, by me.", value="{} - {}".format(str(bio), args))
                    embed.set_author(name="Add gearBot to your server",  url=keys.invite_bot, icon_url="https://n0tj.com/g_center.png")
                    embed.set_footer(text=keys.announcement, icon_url="https://n0tj.com/buddha.jpeg")
                    await ctx.send( embed=embed)
                    #Logging
                    await logger.bigLog.log_6(ctx,str_user,str(getTag))       
            else:
                search = keys.fourofour
                session = aiohttp.ClientSession()
                response = await session.get('http://api.giphy.com/v1/gifs/search?q=' + search + '&api_key=uBR4zyVetEKJaVob3bNwd3CJHNsmiEf2&limit=50')
                data = json.loads(await response.text())
                gif_choice = random.randint(0, 50)
      
                embed = discord.Embed(colour=discord.Colour(0xa9219b))
                embed.set_thumbnail(url=mentionAvatar)
                #time.sleep(0.5)
                embed.set_author(name="Join the gearBot discord", url=keys.invite_discord, icon_url="https://n0tj.com/g_center.png")
                embed.set_footer(text=keys.announcement, icon_url="https://n0tj.com/buddha.jpeg")
                embed.add_field(name="Hey there,", value="**{} isn't in the database. Type !gear for more information.**".format(args))
                try:
                    embed.set_image(url=data['data'][gif_choice]['images']['original']['url'])
                except IndexError:
                    print("Failed to grab gif.")
                    await logger.bigLog.log_9()
                await ctx.send(embed=embed)



        #This is some santization of input, when the user passes a link it verifies it is a link by checking to see if its starts with 'http'
        #Try to cover more edge cases here for example if the user passes an invalid link or if they pass garbage instead of a link or a invalid users @.
        if await urlChecker.urlCheck(urlChecker.session, args) is False:
            await ctx.send("Your link is invalid - try another.")
        else:
            if args.startswith("http") and await urlChecker.urlCheck(urlChecker.session, args) is True:
                name = str(ctx.author)
                authorID = str(ctx.author.id)
         
                r = await db_sessions.dyno_check_user(authorID) #Updated to DynamoDB

                if authorID == r:
                    #This try/except fixes the issue if a user updates their discord_tag
                    try: 
                        await db_sessions.dyno_update_info(str(ctx.author.id), str(name), args, '!gearbio <cool things about me>',  str(datetime.datetime.now()), str(ctx.guild), dynamodb=None) #Updated to DynamoDB
                        await ctx.send("Your profile has been updated.")
                    except:
                         await db_sessions.dyno_insert_user(str(ctx.author.id), str(name), args, str(ctx.guild)) #Updated to DynamoDB
                         await ctx.send("You might of changed your discord tag, so we went ahead and added you back to the database.")
                    #Logging
                    await logger.bigLog.log_1(ctx,str_user)
                else:
                    await db_sessions.dyno_insert_user(str(ctx.author.id), str(name), args, str(ctx.guild)) #Updated to DynamoDB
                    await ctx.send("You have been added to the database.")
                    #Logging
                    await logger.bigLog.log_2(ctx,str_user)

            #if args.startswith("http") or args.startswith("<"):
            #    print("User invoked command.")
                #mentionID = str(ctx.message.mentions[0].id)
                #print(mentionID)
           # else:
           #     embed = discord.Embed(colour=discord.Colour(0xa9219b))
           #     embed.set_thumbnail(url="https://n0tj.com/g_center.png")
           #     embed.set_author(name="Join the gearBot discord", url="https://discord.gg/jZAJ7Yy", icon_url="https://n0tj.com/g_center.png")
           #     embed.set_footer(text=keys.announcement, icon_url="https://n0tj.com/buddha.jpeg")
            #    embed.add_field(name="**Updating your gear screenshot, direct link only**", value="**!gear <link>**")
            #    embed.add_field(name="**Looking up someone or your own gear**", value="**!gear <@user>**")
            #    await ctx.send(embed=embed)

    @commands.command(name='gearbio')
    async def gearbio(self, ctx, *args):

        bio = (" ".join(args[:]))

        if len(args) < 100:
            authorID = str(ctx.author.id)
            name = ctx.author
            getLink = await db_sessions.dyno_get_link(authorID)
            print(name)
            print(str(authorID))
            print(getLink)
            #print(str(getLink))
            await db_sessions.dyno_update_info(str(ctx.author.id), str(name), str(getLink), str(bio), str(datetime.datetime.now()), str(ctx.guild), dynamodb=None) #Updated to DynamoDB
            await ctx.send("Your bio has been updated.")
        else:
            await ctx.send("Your bio can't exceed 250 characters.")
        


#Adding this as a cog
def setup(bot):
    bot.add_cog(gear_Cog(bot))
