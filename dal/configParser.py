from configparser import ConfigParser

class configFile():
    global CONFIG_FILE
    CONFIG_FILE = 'config.ini'
    global config
    config = ConfigParser()
    config.read(CONFIG_FILE)

    def getValue(section, key):
        return config.get(section, key)

    def saveValue(section, key, value):
        if section in config.sections():
            config.set(section, key, value)
            with open(CONFIG_FILE, "w") as file:
                config.write(file)
        
        else:
            config.add_section(section)
            config.set(section, key, value)
            with open(CONFIG_FILE, "w") as file:
                config.write(file)