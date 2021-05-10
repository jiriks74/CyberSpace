from firebase import Firebase

from dal.configParser import configFile

class database:
    config = {
        "apiKey": configFile().getValue('secrets', "apiKey"),
        "authDomain": configFile().getValue('secrets', "authDomain"),
        "databaseURL": configFile().getValue('secrets', 'databaseURL'),
        "storageBucket": configFile().getValue('secrets', "storageBucket")
        } # Init the configuration with data from settings file
    firebase = Firebase(config) # Init firebase with the config

    def test_connection(self):
        pass # TODO connection test