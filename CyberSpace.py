import discord
from discord.ext import commands

from templates.confParsTemp import confParsTemp # Import config parser template
from dal.database import database # Import database data access layer
class client():
    def setup():
        if confParsTemp().createIfNone(): # Run config template, so if no config.ini exists, one will be created, and if created, app will exit needing to fill secrets
            print("Please fill [secrets] section in config.ini")
            exit()
        database().test_connection()



if __name__ == "__main__":
    client.setup()