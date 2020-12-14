<p>
<img src= https://img.shields.io/github/last-commit/n0tj/gearBot.svg />
<a href="https://discordbots.org/bot/344643767313235968" >
  <img src="https://discordbots.org/api/widget/servers/344643767313235968.svg" alt="gearBot" />
</a>
<a href="https://discordbots.org/bot/344643767313235968" >
  <img src="https://discordbots.org/api/widget/status/344643767313235968.svg" alt="gearBot" />
</a>
</p>

<center><img src="https://i.imgur.com/ldtc2Qk.png"/></center>
Screenshot and bio database.
A lot of this configuration doesn't follow best practices, please harden your server/database user privileges arrcodingly. This is simply to get your bot stood up with ease.


## General Use
>!gear or !gearhelp will give you the help commands.


>!gear <@link> will update you your gear screenshot in the database.
 

>!gear <@user> will query the database for a users gear screenshot and share it to the channel where requested.



## Build
### Download the discord.py library 
> python3 -m pip install -U discord.py
### Install all the depencies of the bot
> pip install -r requirements.txt

### We have to add a path in bash, so main.py can reach into the cog modules
> nano ~/.bashrc

Append the following to the bottom of the file

> export PYTHONPATH="/PATH/TO/gearBot/cogs/modules"

Save the file and then run the following

> source ~/.bashrc


## Final Step
Navigate  to the keys.py file and enter all the information missing.

## Optional
If you want to get the bot to restart on restart we can utilize cronjobs and screen.
> sudo contrab -e

> @reboot sleep 20 && export PYTHONPATH="/root/gearBot/cogs/modules" && screen -dmS 'bot' bash -c 'cd /root/gearBot; export PYTHONPATH="/root/gearBot/cogs/modules"; python3 main.py; bash' 2>&1

If you get a module error, move all the files from *modules* into *cogs* and then edit gear.py and gearhelp.py to import from *cogs.modules* to *cogs*



## Contact me
If you have any questions you can contact me via discord, ping me a lot; n0tj#6859 

