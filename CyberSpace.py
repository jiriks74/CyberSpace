import discord
from discord.ext import commands

from disapi.discordConnect import client
from templates.confParsTemp import confParsTemp # Import config parser template
#from dal.sqlite import sqlite as database # Import database data access layer
from dal.firebase import firebase as database
from dal.configFile import configFile

class main():

    def setup(self):
        if confParsTemp().createIfNone(): # Run config template, so if no config.ini exists, one will be created, and if created, app will exit needing to fill secrets
            print("Please fill [secrets] section in config.ini")
            exit()

        bot = client()
        print("complete")


if __name__ == "__main__":
    main().setup()