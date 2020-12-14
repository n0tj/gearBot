import discord
from discord.ext import commands
import db_sessions
import datetime
import logging
from datetime import datetime


f = open("log.txt", "a")
logging.basicConfig(filename='log.txt', filemode='a', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.WARNING)
#logging.getLogger("requests").setLevel(logging.WARNING)
#logging.getLogger("urllib3").setLevel(logging.WARNING)

class bigLog:
    async def log_1(ctx,str_user):
        print("##########################")
        print(datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)"))
        print("Server: {}".format(ctx.guild))
        print("Valid Link.")
        print("{} is in the database.".format(str_user))
        print ("{} updated their gear link.".format(str_user))
        logging.warning("Updated {} link! \n".format(str_user))
      
    async def log_2(ctx,str_user):
        print("##########################")
        print(datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)"))
        print("Server: {}".format(ctx.guild))
        print ("{} has been added to the database.".format(str_user))
        logging.warning("{} has been added to the database! \n".format(str_user))

        
    async def log_3(ctx,str_user):
        print("##########################")
        print(datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)"))
        print("Server: {}".format(ctx.guild))
        print ("{} tried to update their ap or dp with invalid data".format(str_user))
        logging.warning("{} tried to update with invalid AP and or DP. \n".format(str_user))
      
    async def log_4(ctx,str_user):
        print("##########################")
        print(datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)"))
        print("Server: {}".format(ctx.guild))
        print ("{} updated their gear, ap and dp.".format(str_user))
        logging.warning("{} updated their ap and dp! \n".format(str_user))


    
    async def log_5(ctx,str_user,getTag):
        print("##########################")
        print("Legacy Layout")
        print(datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)"))
        print("Server: {}".format(ctx.guild))
        print ("{} looked up {}'s gear".format(str_user, getTag))
        logging.warning("{} updated their ap and dp! \n".format(str_user))

   
    async def log_6(ctx,str_user,getTag):
        print("##########################")
        print(datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)"))
        print("Server: {}".format(ctx.guild))
        print ("{} looked up {}'s gear".format(str_user,getTag))
        logging.warning("{} looked up {} with the improved layout. \n".format(str_user,getTag))

    async def log_7(ctx,str_user):
        print("##########################")
        print(datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)"))
        print("Server: {}".format(ctx.guild))
        print ("{} toggled gearhelp!".format(str_user))

    async def log_8(ctx,str_user):
        print("##########################")
        print(datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)"))
        print("Server: {}".format(ctx.guild))
        print ("{} toggled link help!".format(str_user))

    async def log_9():
        print("##########################")
        print(datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)"))
        print ("GIF failed to load.")
        logging.warning("{}: Failed at loading the gif.\n".format(datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)")))