import pymysql

class DBMS:
    def __init__(self):
        # Initialize the connection and cursor as instance variables
        self.conn = pymysql.connect(
            host='localhost',
            user='root',
            password='Your Password',
            database='Your DataBase'
        )
        self.cursor = self.conn.cursor()
        self.cursor.execute('USE costruction_management_system')  # Not necessary if database is already specified
    
    def add_data(self, user_name, material_name, material_quant, unit_price, category, supplier_name ='same', builder_name='same'):
        # Use parameterized query to prevent SQL injection
        query = """
        INSERT INTO construction_record 
        (user_name, material_name, material_quantity, unit_price, category, suplier_name, builder_name)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        values = (user_name, material_name, material_quant, unit_price, category, supplier_name, builder_name)
        self.cursor.execute(query, values)
        self.conn.commit()  
    def remove_data(self,value):
        query = """DELETE FROM construction_record WHERE material_name = %s"""
        self.cursor.execute(query, (value,))
        self.conn.commit()
    def update_data(self,value,option,name):
        if option == '1':
            query = """ UPDATE construction_record 
            SET material_quantity = %s
            WHERE user_name = %s
            """
            self.cursor.execute(query,(value,name))
        elif option == '2':
            query = """ UPDATE construction_record 
            SET unit_price = %s
            WHERE user_name = %s
            """
            self.cursor.execute(query,(value,name))
