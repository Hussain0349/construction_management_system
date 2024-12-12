from name import Name
from sqlwithpython import DBMS
class User(Name):
    def __init__(self,name):
        super().__init__(name)
        self.__materials = []   
        self.__suplier = {}  
        self.__builder = {}
        self.__totalCost = 0
    
    def add_product(self,material):
        self.__materials.append(material)

    def addSuplierAndBuilder(self,suplier,builder):
        self.__suplier['Name'] = suplier.getName()
        self.__suplier['Address'] = suplier.getAddress()
        self.__suplier['contact info'] = suplier.getContactInfo()
        self.__builder['Name'] = builder.getName()
        self.__builder['Address'] = builder.getAddress()
        self.__builder['contact info'] = builder.getContactInfo()
        print('Suplier & Builder Added Successfully ')
    def updateQuantity(self,name):
        option = input('Enter 1 for (quanity) and 2 for unit_price')
        found = False
        for meterial in self.__materials:
            if meterial.getName() == name:
                if option == '1':
                    new_quantity = int(input('Enter new quantity: '))
                    meterial.setQuantity(new_quantity)
                    name = meterial.getName()
                    d1 = DBMS()
                    d1.update_data(new_quantity,option,name)
                    print('Quantity Updated Successfully')
                    found = True
                    break
                elif option == '2':
                    unit_price = input('Enter New Unit Prce: ')
                    meterial.setUnitPrice(unit_price)
                    d1 = DBMS()
                    d1.update_data(new_price,option,name)
                    print('Unit Price Updated Successfully')
                    found = True
                    break
        if not found:
            print('Material Not Found')

    def getSupplier(self):
        return self.__suplier


    def remove_product(self,name):
        found = False
        for meterial in self.__materials: 
            if meterial.getName() == name:
                self.__materials.remove(meterial)
                d1 = DBMS()
                material_name = meterial.getName()
                d1.remove_data(material_name)
                print(f'{material_name} is  Removed Successfully')
                found = True
                break
        if not found:
            print('Material is not Exist') 

    def generate_receipt(self):
        print("Your Record".center(40))
        print("*" * 40)

        supplier = self.__suplier
        print(f"Supplier:".ljust(20) + supplier['Name'])
        print(f"Address:".ljust(20) + supplier['Address'])
        print(f"Contact Info:".ljust(20) + supplier['contact info'])

        builder = self.__builder
        print(f"Builder:".ljust(20) + builder['Name'])
        print(f"Address:".ljust(20) + builder['Address'])
        print(f"Contact Info:".ljust(20) + builder['contact info'])

        print("-" * 40)

        print(f"{'Item':<20}{'Price':>10}")
        total = 0
        for material in self.__materials:
            name = material.getName()
            price = material.getUnitPrice() * material.getQuantity()
            total += price
            print(f"{name:<20}{price:>10.2f}")

        print("-" * 40)

        print(f"{'Total:':<30}{total:>10.2f}")
    
        print("Thank you To Using This App!".center(40))

