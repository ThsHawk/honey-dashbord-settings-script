import os
import sys
import json
from src.Service import Service

def searchService(list, service):
    for i in range(len(list)):
        if list[i]["name"] == service:
            return i
    return -1

def openFile(mode):
    argvLen = len(sys.argv)
    if argvLen < 2:
        print("Err: Too few arguments!")
        exit()
    elif argvLen > 3:
        print("Err: Too many arguments!")
        exit()
    else:
        try:
            file = open(sys.argv[1], mode)
        except FileNotFoundError:
            print("Err: File \'" + sys.argv[1] + "\' not found.")
            exit()
        return file
    
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
            newService = dict(name="", desc="", href="", icon="")
            new = Service()
            new.setName()
            newService["desc"] = input("Service description: ")
            newService["href"] = input("Link to service (blank to default): ")
            if not newService["href"]: newService["href"] = newService["name"].lower()
            newService["icon"] = input("Path to icon (blank to default): " or "img/preview/default.png")
            if not newService["icon"]: newService["icon"] = "img/preview/default.png"
            services.append(newService)
            settings["services"] = services
        case "3":
            serviceName = input("Service name: ")
            serviceIndex = searchService(services, serviceName)
            
            print(services)
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
