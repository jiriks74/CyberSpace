import discord
from discord.ext import commands

from templates.confParsTemp import confParsTemp
from dal.database import database
class client():
    def setup():
        confParsTemp().createIfNone()
        database.test_connection()



if __name__ == "__main__":
    client.setup()