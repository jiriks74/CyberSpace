from configparser import ConfigParser

class configFile():
    """
    Class for interaction with config.ini file
    """
    global CONFIG_FILE
    CONFIG_FILE = 'config.ini'
    global config
    config = ConfigParser() # Create config parser so the program can interact with ini files
    config.read(CONFIG_FILE) # Load data from CONFIG_FILE (default config.ini)

    def getValue(self, section, key):
        """
        Returns a value set in CONFIG_FILE (default config.ini)

        section - section name in config.ini\n
        key - key name in config.ini
        """
        return config.get(section, key) # Gets the key value from key set in section

    def saveValue(self, section, key, value):
        """
        Saves value to CONFIG_FILE (default config.ini)
        
        section - section name where the key will be\n
        key - key name\n
        value - value of the key
        """
        if section in config.sections(): # If the section already exists
            config.set(section, key, value) # Set value of a key (if the key doesn't exist, it will be created)
            with open(CONFIG_FILE, "w") as file: # Write the changes to CONFIG_FILE (default config.ini)
                config.write(file)
        
        else: # If the section doesn't exist
            config.add_section(section) # Create the section
            config.set(section, key, value) # Add the key with it's value
            with open(CONFIG_FILE, "w") as file: # Save changes to CONFIG_FILE (default config.ini)
                config.write(file)