from firebase import Firebase

from dal.configParser import configFile

class database:
    config = {
        "apiKey": configFile().getValue('secrets', "apiKey"),
        "authDomain": configFile().getValue('secrets', "authDomain"),
        "databaseURL": configFile().getValue('secrets', 'databaseURL'),
        "storageBucket": configFile().getValue('secrets', "storageBucket")
        }
    firebase = Firebase(config)

    def test_connection(self):
        pass