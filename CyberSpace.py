import discord
from discord.ext import commands

from disapi.discordConnect import client
from templates.confFileTemp import confFileTemp # Import config parser template
#from dal.firebase import firebase as database

class main():

    def setup(self):
        if confFileTemp().createIfNone(): # Run config template, so if no config.ini exists, one will be created, and if created, app will exit needing to fill secrets
            print("Please fill [secrets] section in config.ini")
            exit()

        client()


if __name__ == "__main__":
    main().setup()