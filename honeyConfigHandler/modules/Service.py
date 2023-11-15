# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

#from icecream import ic

# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

class Service():
    # ---------------------------
    # constructor
    # ---------------------------
    def __init__(self):   
        
        self.name = "name"
        self.desc = "description"
        self.href = "https://classify.fun"
        self.icon = "img/preview/default.png"
                        
    # ---------------------------
    # setters
    # ---------------------------
    def setName(self, name=None):
        if name == None:
            while not name:
                name = input("Service name: ")
                if not name: print("Err: null string.")
            self.name = name
        else:
            self.name = name
            
    def setDesc(self, desc=None):
        if desc == None:
            while not desc:
                desc = input("Service brief: ")
                if not desc: print("Err: null string.")
            self.desc = desc
        else:
            self.desc = desc
            
    def setHref(self, href=None):
        if href == None:
            while not href:
                href = input("Service link: ")
                if not href: print("Err: null string.")
            self.href = href
        else:
            self.href = href
            
    def setIcon(self, icon=None):
        if icon == None:
            icon = input("Service icon: ")
            if not icon: icon  = "img/preview/default.png"
            self.icon = icon
        else:
            self.icon = icon

    # ---------------------------
    # getters
    # ---------------------------
    def getName(self):
        return self.name
    
    def getDesc(self):
        return self.desc
    
    def getHref(self):
        return self.href
    
    def getIcon(self):
        return self.icon

# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------