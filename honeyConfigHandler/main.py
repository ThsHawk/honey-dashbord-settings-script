# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

import json

from modules.Service import Service
from modules.FileHandler import openFile

# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

# ---------------------------
# linear search
# ---------------------------
def searchService(list, service):
    for i in range(len(list)):
        if list[i]["name"] == service:
            return i
    return -1
    
# ---------------------------
# menu options
# ---------------------------
def menu(settings):
    services = settings.get("services")
    print("-- Services Manager Script --")
    print("01 - List services")
    print("02 - Add service")
    print("03 - Del service")
    print("05 - Edit service")
    print("05 - Exit\n")
    
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
            settings["services"] = services
        case "3":
            serviceName = input("Service name: ")
            serviceIndex = searchService(services, serviceName)
            services.pop(serviceIndex) if serviceIndex != -1 else print("Err: Service not found.\n")
            settings["services"] = services
        case "4":
            serviceName = input("Service name: ")
            serviceIndex = searchService(services, serviceName)
            services.pop(serviceIndex) if serviceIndex != -1 else print("Err: Service not found.\n")
            settings["services"] = services
        case "5":
            return 0
        case _:
            print("Err: invalid option.")
    return 1

# ---------------------------
# main
# ---------------------------              
def main():
    file = openFile("r")
    settings = json.load(file)
    file.close()

    flag = 1
    while flag:
        flag = menu(settings)
        
    file = openFile("w")
    json.dump(settings, file, indent="\t", separators=(', ', ': '))
    file.close()
    
main()
