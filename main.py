from builder import Builder
from material import Material
from supplier import Supplier
from user import User
from sqlwithpython import DBMS
users = []
def main():
        print("""
        -----------------------------------------------
        |                                             |
        |                                             |
        |                                             |
        |       Construction Management System        +
        +              Here You Saved                 +
        +                  Your                       +
        +                 Recored                     |
        |                                             |
        |                                             |
        |                                             |
        -----------------------------------------------
        """)
        op = input("""
            1) To  Add Material
            2) To Remove Material
            3) To Update Material
            4) Check Your Summary
            5) For Tests
        """)

        if op == '1':
            name = input('Enter Your Name: ')
            found = False
            for user in users:
                if user.getName() == name:
                    found = True
                    material = input('Material Name: ')
                    material_quantity = int(input('Material Quantity: '))
                    unit_price = float(input('Unit Price: '))
                    material_category = input('Material Category: ')
                    d1 = DBMS()
                    d1.add_data(name,material,material_quantity,unit_price,material_category)
                    m1 = Material(material,material_quantity,unit_price,material_category)
                    user.add_product(m1) 
                    break
 
            if not found:
                us1 = User(name)
                material = input('Material Name: ')
                material_quantity = int(input('Material Quantity: '))
                unit_price = float(input('Unit Price: '))
                material_category = input('Material Category: ')
                suplier_name = input('Enter Suplier Name: ')
                suplier_address = input('Enter Suplier Address: ')
                suplier_contact = input('Enter suplier Contact info: ')
                builder_name = input('Enter Builder Name: ')
                builder_address = input('Enter Builder Address: ')
                builder_contact = input('Enter Builder Contact info: ')
                d1 = DBMS()
                d1.add_data(name,material,material_quantity,unit_price,material_category,suplier_name,builder_name)
                m1 = Material(material,material_quantity,unit_price,material_category)
                b1 = Builder(builder_name,builder_address,builder_contact)
                s1 = Supplier(suplier_name,suplier_address,suplier_contact)
                us1.addSuplierAndBuilder(s1,b1)
                us1.add_product(m1)
                users.append(us1)
            main()
        elif op == '2':
            name = input('Enter Your Name: ')
            found = False
            for user in users:
                if user.getName() == name:
                    Material_name = input('Material you want to remove: ')
                    user.remove_product(Material_name)
                    found = True
                    break
            if not found:
                print('User Not Found! ')
            main()
        
        elif op == '3':
            name = input('Enter Your Name: ')
            found = False
            for user in users:
                if user.getName() == name:
                    material_name = input('Enter material name: ')
                    user.updateQuantity(material_name)
                    found = True
                    main()
            if not found:
                print('User Not Found')
            main()
        elif op == '4':
            name = input('Enter Your Name: ')
            for user in users:
                if user.getName() == name:
                    user.generate_receipt()
            
                

        
            
        

main()
