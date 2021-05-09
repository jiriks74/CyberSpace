import discord
from discord.ext import commands

from templates.confParsTemp import confParsTemp
class client():
    def setup():
        if confParsTemp().createIfNone():
            from dal.database import database
        
        database().test_connection()



if __name__ == "__main__":
    client.setup()