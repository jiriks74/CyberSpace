from firebase import Firebase

from dal.configParser import ConfigParser

class database:
    config = {
        "apiKey": ConfigParser().getValue('secrets', "apiKey")
        "authDomain": ConfigParser().getValue('secrets', "authDomain")
        "databaseURL": ConfigParser().getValue('secrets', 'databaseURL'),
        "storageBucket": ConfigParser().getValue('secrets', "storageBucket")
        }
    firebase = Firebase(config)

    def test_connection(self):
        pass