from name import Name

class Material(Name):
    def __init__(self,name,quantity,unit_price,category):
        super().__init__(name) 
        self.__quantity = quantity
        self.__unit_price = unit_price
        self.__category = category


    def getUnitPrice(self):
        return self.__unit_price
    
    def getQuantity(self):
        return self.__quantity
    def getCategory(self):
        return self.__category


    def setQuantity(self,quantity):
        self.__quantity +=quantity

    def setUnitPrice(self,price):
        self.__unit_price = price

    

    def __str__(self):
        return     f'Name: {self._Name__name}\n Material Quantity: {self.__quantity}\n Unit Price: {self.__unit_price}\n Catgeory: {self.__category}'
