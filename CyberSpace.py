from discord.ext import commands

from dal.configFile import configFile
from disapi.discordConnect import client
from templates.confFileTemp import confFileTemp # Import config parser template
from misc.misc import console

class main():

    def __init__(self):
        console().clear()

    def setup(self):
        if confFileTemp().createIfNone(): # Run config template, so if no config.ini exists, one will be created, and if created, app will exit needing to fill secrets
            configFile().saveValue('secrets', 'bot_token', input("Please insert your discord token and press enter:\n"))
            console().clear()
            configFile().saveValue('secrets', 'databaseURL', input("Please insert URL to your firebase database and press enter:\n"))
            console().clear()

        client()

if __name__ == "__main__":
    main().setup()