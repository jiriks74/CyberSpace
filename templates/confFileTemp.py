from os import path, mkdir
from configparser import ConfigParser

from dal.configFile import configFile
class confFileTemp():
    """
    Class for configParser template data/config.ini
    """
    DATA_FOLDER = configFile().DATA_FOLDER
    CONFIG_FILE_PATH = configFile().CONFIG_FILE_PATH
    config = ConfigParser()
    def createIfNone(self):
        """
        Creates CONFIG_FILE (default config.ini) if none exists

        Returns False, if file exists, returns True if template was created
        """
        if path.exists(self.CONFIG_FILE_PATH): # If file exists, just return False
            return False

        else: # If the file doesn't exist, create template datastructure with default values and return True
            secrets = "secrets"
            self.config.add_section(secrets)
            self.config.set(secrets, 'bot_token', 'yourBotToken')
            self.config.set(secrets, 'databaseURL', 'yourDatabaseURL')

            bot = 'bot'
            self.config.add_section(bot)
            self.config.set(bot, 'bot_name', 'CyberSpace')
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

            If your team is ready, captain can start game with command `start`
            ''')

            if not path.exists(self.DATA_FOLDER):
                mkdir(self.DATA_FOLDER)

            with open(self.CONFIG_FILE_PATH, "w") as file:
                self.config.write(file)
            
            return True