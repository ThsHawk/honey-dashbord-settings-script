# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

import json

from modules.Service import Service
from modules.FileHandler import openFile
from modules.DatabaseHandler import DatabaseHandler 

# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

class Options():
    # ---------------------------
    # constructor
    # --------------------------- 
    def __init__(self):

        self.configPath = input("config.json file absolute path: ")
        self.dbConfigPath = input("DB config file absolute path: ")
        file = openFile("r", self.configPath)
        self.settings = json.load(file)
        self.services = self.settings.get("services")
        file.close()

    # ---------------------------
    # destructor
    # ---------------------------
    def __del__(self):
        self.settings["services"] = self.services
        file = openFile("w", self.configPath)
        json.dump(self.settings, file, indent="\t", separators=(', ', ': '))
        file.close() 
    
    # ---------------------------
    # menu
    # ---------------------------
    def menu(self):
        print("-- Services Manager Script --")
        print("01 - List services")
        print("02 - Add service")
        print("03 - Del service")
        print("04 - Edit service")
        print("05 - Load from Database")
        print("06 - Load into Database")
        print("07 - Flush Database")
        print("08 - Exit\n")
        
        opt = input("Select an option (default = 1): ")
        if not opt: opt = "1"
        print("\n")
        
        match opt:
            case "1":
                self.list()
            case "2":
                self.add()
            case "3":
                self.remove()
            case "4":
                self.remove()
                self.add()
            case "5":
                self.dbLoad()
            case "6":
                self.dbInsert()
            case "7":
                self.dbFlush()
            case "8":
                return 0
            case _:
                print("Err: invalid option.")
        return 1
    
    # ---------------------------
    # list available services
    # ---------------------------
    def list(self):
        print("\nServices available:")
        for i in range(len(self.services)):
            print(self.services[i]["name"])
        print("\n")
    
    # ---------------------------
    # add new service
    # ---------------------------
    def add(self):
        newService = Service()
        newService.setName()
        newService.setDesc()
        newService.setHref()
        newService.setIcon()
        self.services.append(newService.__dict__)

    # ---------------------------
    # remove service
    # ---------------------------
    def remove(self):
        serviceName = input("Service name: ")
        serviceIndex = self.searchService(serviceName)
        self.services.pop(serviceIndex) if serviceIndex != -1 else print("Err: Service not found.\n")

    # ---------------------------
    # load services from database
    # ---------------------------
    def dbLoad(self):
        db = DatabaseHandler(self.dbConfigPath)
        self.services = db.loadServices()
    
    # ---------------------------
    # insert services into database
    # ---------------------------
    def dbInsert(self):
        db = DatabaseHandler(self.dbConfigPath)
        db.insertServices(self.services)
    
    # ---------------------------
    # flush services
    # ---------------------------
    def dbFlush(self):
        db = DatabaseHandler(self.dbConfigPath)
        db.flush(self.services)
    
    # ---------------------------
    # set path variables
    # ---------------------------
    def setPath(self, configPath, dbConfigPath):
        self.configPath = configPath
        self.dbConfigPath = dbConfigPath
   
    # ---------------------------
    # linear search
    # ---------------------------
    def searchService(self, service):
        for i in range(len(self.services)):
            if self.services[i]["name"] == service:
                return i
        return -1

# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------