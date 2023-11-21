# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

import mariadb
import json
import logging

from modules.FileHandler import openFile
from modules.Service import Service

# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

class DatabaseHandler():
    # ---------------------------
    # constructor
    # --------------------------- 
    def __init__(self):

        filePath = input("DB config file absolute path: ")
        file = openFile("r", filePath)
        config = json.load(file)
        file.close()
        
        try:
            self.dbConn = mariadb.connect(**config)
            self.db = self.dbConn.cursor()
        except Exception as err:
            print("Err")

    def __init__(self, filePath):

        file = openFile("r", filePath)
        config = json.load(file)
        file.close()
        
        try:
            self.dbConn = mariadb.connect(**config)
            self.db = self.dbConn.cursor()
        except Exception as err:
            print("Err")

    # ---------------------------
    # destructor
    # ---------------------------
    def __del__(self):
        logging.debug("Encerrando conexão com o Banco de Dados.")
        self.db.close()
        self.dbConn.close()   
    
    # ---------------------------
    # load services from database
    # ---------------------------
    def loadServices(self):
        self.db.execute("SELECT * FROM services")
        dbSearch = self.db.fetchall()
        if dbSearch == None:
            return []
        else:
            services = []
            for i in range(len(dbSearch)):
                service = Service()
                service.setName(dbSearch[i][0])
                service.setDesc(dbSearch[i][1])
                service.setIcon(dbSearch[i][2])
                service.setHref(dbSearch[i][3])
                services.append(service.__dict__)
            return services

    # ---------------------------
    # insert services into database
    # ---------------------------    
    def insertServices(self, services):
        for i in range(len(services)):
            print(services[i]["name"])
            self.db.execute("INSERT INTO services(name, brief, icon, href) VALUES (?, ?, ?, ?)",
                            (services[i]["name"], services[i]["desc"], services[i]["icon"], services[i]["href"]))
        self.dbConn.commit()

    # ---------------------------
    # flush all services on database
    # ---------------------------     
    def flush(self):
        self.db.execute("DELETE FROM services")
# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------