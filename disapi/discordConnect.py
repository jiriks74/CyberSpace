import asyncio
import os, sys
import discord
from discord.ext import commands

from dal.configFile import configFile
from misc.misc import timeStr, console
#from disapi.commands import bot_commandent

class client():
    """
    Bot client class

    On initialization, bot connects to discord with token from config.ini
    """
    bot = commands.Bot(command_prefix="?") # Initialize bot
    def __init__(self):
        print("Initializing...")

        try:
            self.bot.run(configFile().getValue('secrets', 'bot_token')) # Start the bot and connect it to discord

        except discord.errors.LoginFailure as e:
            print(e)
            print("======================================\nBot login unsuccessful.")
            configFile().saveValue('secrets', 'bot_token', input("Probably improper token. Please insert proper token and press enter:\n"))
            console().clear()
            os.execl(sys.executable, os.path.abspath(__file__), *sys.argv) 
            
    @bot.event
    async def on_ready():
        """
        Runs after bot is connected to discord successufully

        Prints bot info to console
        """
        print('\033c')
        print(configFile().getValue('bot', 'bot_name')+' - version: 0.1.0 Created by CyberCity dev team https://discord.gg/NdrhvcF')
        print(client.bot.user.name+' ('+str(client.bot.user.id)+')'' is successfuly connected (at '+timeStr().getTime()+')')
        print('-------------------------------------------------------------------------------')


class bot_commands():
    @client.bot.command(pass_context=True)
    async def ping(message):
        await message.channel.send("pong")