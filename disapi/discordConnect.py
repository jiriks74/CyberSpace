import asyncio
import discord
from discord.ext import commands

from dal.configFile import configFile
from misc.timeStr import timeStr
#from disapi.commands import bot_commandent

class client():
    bot = commands.Bot(command_prefix="?")
    def __init__(self):
        print("initializing...")
        self.bot.run(configFile().getValue('secrets', 'bot_token'))

    @bot.event
    async def on_ready():
        start = timeStr()
        print('\033c')
        print(configFile().getValue('bot', 'bot_name')+' - version: 0.1.0 Created by CyberCity dev team https://discord.gg/NdrhvcF')
        print(client.bot.user.name+'( '+str(client.bot.user.id)+' )'' is successfuly connected (at '+start.getTime()+')')
        print('-------------------------------------------------------------------------------')


class bot_commands():
    bot = client
    @client.bot.command(pass_context=True)
    async def ping(message):
        await message.channel.send("pong")