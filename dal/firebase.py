from os import path
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
import json

from dal.configFile import configFile

class firebase():
    global cred
    global ref

    def __init__(self):
        if not path.exists("data/firebase-cred.json"):# zápis dat do databáze
            print("Missing `data/firebase-cred.json` file in dal folder. Get this file in your project settings on https://console.firebase.google.com\nIf you haven't, set database url in config.ini")
            exit()

        else:
            self.cred = credentials.Certificate("data/firebase-cred.json")     # Cesta k jsou souboru s přístupovými údaji
            # firebase_admin.initialize_app(cred)
            firebase_admin.initialize_app(self.cred, {'databaseURL': configFile().getValue('secrets', 'databaseURL')})

            self.ref = db.reference("/")     # Nastavení rootu

    def test(self):                                        
        with open('data/data.json', 'r') as d: # Načtení dat (může být ze souboru jako teď, nebo se může složit se streamu a poslat)
            data = json.load(d)

        self.ref.set(data)