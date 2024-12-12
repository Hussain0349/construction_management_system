class Name:
    def __init__(self,name,address='',contact_info=''):
        self.__contact_info = contact_info
        self.__address = address
        self.__name = name
    
    def getName(self):
        return self.__name
    def getAddress(self):
        return self.__address
    def getContactInfo(self):
        return self.__contact_info

    def setName(self,newName):
        setName = newName

    def __str__(self):
        return f'name: {self.__name}\n Address: {self.__address}\n contact Info: {self.__contact_info}'
