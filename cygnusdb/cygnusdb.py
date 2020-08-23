import json
import os

class CygnusDB(object): # Main Class
    def __init__(self , location):
        self.location = os.path.expanduser(location)
        self.load(self.location)

    # Load database file
    def load(self , location):
       if os.path.exists(location):
           self._load() # calls _load
       else:
            self.db = {}
       return True

    # Load database file (2)
    def _load(self):
        self.db = json.load(open(self.location , "r"))

    def dumpdb(self):
        try:
            json.dump(self.db , open(self.location, "w+"))
            return True
        except:
            return False

    # Set data under name + variable
    def set(self , key , value):
        try:
            self.db[str(key)] = value
            self.dumpdb()
        except Exception as e:
            print("[CygnusDB] Error saving value to database: " + str(e))
            return False

    # Return data
    def get(self , key):
        try:
            return self.db[key]
        except KeyError:
            print("[CygnusDB] Nothing found in the database for: " + str(key))
            return False

    # Delete specified data
    def delete(self , key):
        if not key in self.db:
            return False
        del self.db[key]
        self.dumpdb()
        return True
    
    # Resets database
    def resetdb(self):
        self.db={}
        self.dumpdb()
        return True