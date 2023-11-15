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
        file.close()

    # ---------------------------
    # destructor
    # ---------------------------
    def __del__(self):
        file = openFile("w", self.configPath)
        json.dump(self.settings, file, indent="\t", separators=(', ', ': '))
        file.close() 
    
    # ---------------------------
    # menu
    # ---------------------------
    def menu(self):
        services = self.settings.get("services")
        print("-- Services Manager Script --")
        print("01 - List services")
        print("02 - Add service")
        print("03 - Del service")
        print("04 - Edit service")
        print("05 - Load from Database")
        print("06 - Exit\n")
        
        opt = input("Select an option (default = 1): ")
        if not opt: opt = "1"
        print("\n")
        
        match opt:
            case "1":
                print("\nServices available:")
                for i in range(len(services)):
                    print(services[i]["name"])
                print("\n")
            case "2":
                newService = Service()
                newService.setName()
                newService.setDesc()
                newService.setHref()
                newService.setIcon()
                services.append(newService.__dict__)
                self.settings["services"] = services
            case "3":
                serviceName = input("Service name: ")
                serviceIndex = self.searchService(services, serviceName)
                services.pop(serviceIndex) if serviceIndex != -1 else print("Err: Service not found.\n")
                self.settings["services"] = services
            case "4":
                serviceName = input("Service name: ")
                serviceIndex = self.searchService(services, serviceName)
                services.pop(serviceIndex) if serviceIndex != -1 else print("Err: Service not found.\n")
                self.settings["services"] = services
            case "5":
                db = DatabaseHandler()
                self.settings["services"] = db.loadServices()
            case "6":
                return 0
            case _:
                print("Err: invalid option.")
        return 1
    
    # ---------------------------
    # linear search
    # ---------------------------
    def searchService(self, list, service):
        for i in range(len(list)):
            if list[i]["name"] == service:
                return i
        return -1

# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------