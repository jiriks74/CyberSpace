from os import path
from configparser import ConfigParser

from dal.configParser import CONFIG_FILE

class confParsTemp():
    """
    Class for configParser template config.ini
    """

    config = ConfigParser()
    def createIfNone(self):
        """
        Creates CONFIG_FILE (default config.ini) if none exists

        Returns False, if file exists, returns True if template was created
        """
        if path.exists(CONFIG_FILE): # If file exists, just return False
            return False

        else: # If the file doesn't exist, create template datastructure with default values and return True
            secrets = "secrets"
            self.config.add_section(secrets)
            self.config.set(secrets, 'botToken', 'yourBotToken')
            self.config.set(secrets, 'apiKey', 'apiKey')
            self.config.set(secrets, 'authDomain', 'projectId.firebaseapp.com')
            self.config.set(secrets, 'databaseURL', 'databaseURL')
            self.config.set(secrets, 'storageBucket', 'projectId.appspot.com')

            bot = 'bot'
            self.config.add_section(bot)
            self.config.set(bot, 'botName', 'CyberSpace')
            self.config.set(bot, 'command_prefix', '?')

            game_creator = 'game_creator'
            self.config.add_section(game_creator)
            self.config.set(game_creator, 'max_channels', '10')
            self.config.set(game_creator, 'max_users', '30')
            self.config.set(game_creator, 'welcome_msg', '''
            Select your class with `{config.get(bot,'command_prefix')}class <number>`
            ```
            1. Captain
            2. Soldier
            3. Medic
            4. Engineer
            5. Chef
            ```
            To start a game at least one of this class is required: Captain, Soldier
            but all class is needed to survive in dark space.

            If your team is ready, captain can start game with command `{config.get(bot,'command_prefix')}start`
            ''')

            with open(CONFIG_FILE, "w") as file:
                self.config.write(file)
            
            return True