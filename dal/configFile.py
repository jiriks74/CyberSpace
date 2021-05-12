from os import path, getcwd
from configparser import ConfigParser

class configFile():
    """
    Class for interaction with .ini files
    """
    DATA_FOLDER = 'data'
    CONFIG_FILE = 'config.ini'
    CONFIG_FILE_PATH = path.join(getcwd(), DATA_FOLDER, CONFIG_FILE)
    config = ConfigParser() # Create config parser so the program can interact with ini files
    config.read(CONFIG_FILE_PATH) # Load data from CONFIG_FILE (default config.ini)

    def getValue(self, section, key):
        """
        Returns a value set in CONFIG_FILE (default config.ini)

        section - section name in config.ini\n
        key - key name in config.ini
        """
        return self.config.get(section, key) # Gets the key value from key set in section

    def saveValue(self, section, key, value):
        """
        Saves value to CONFIG_FILE (default config.ini)
        
        section - section name where the key will be\n
        key - key name\n
        value - value of the key
        """
        if section in self.config.sections(): # If the section already exists
            self.config.set(section, key, value) # Set value of a key (if the key doesn't exist, it will be created)
            with open(self.CONFIG_FILE_PATH, "w") as file: # Write the changes to CONFIG_FILE (default config.ini)
                self.config.write(file)
        
        else: # If the section doesn't exist
            self.config.add_section(section) # Create the section
            self.config.set(section, key, value) # Add the key with it's value
            with open(self.CONFIG_FILE_PATH, "w") as file: # Save changes to CONFIG_FILE (default config.ini)
                self.config.write(file)