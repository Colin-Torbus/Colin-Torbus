import mysql.connector
from mysql.connector import Error
import pandas as pd
from typing import Optional

class Table():
    """Class for database tables."""
    ##FIXME do smth with this.
    def __init__(self):
        mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'EPDS6425',
        database = 'epds_database'
        )
        self.mycursor = mydb.cursor(buffered=True)
        self.mydb = mydb

    def table_pull(self, table, key, data):
        """Checks data from existing table, probably need to change the way it prints"""
        print(self.mycursor.execute(f"""SELECT * FROM {table} WHERE {key} = {data};"""))

    def inventory_check(self, quote_model, count = None):
        """My attempt at checking if we have quote items in stock. Needs improvement.""" ##FIXME
        self.mycursor.execute(f"""SELECT model, num FROM inventory WHERE model='{quote_model}'""")
        # if count > 1:
        #     self.mycursor.execute(f"""SELECT FROM inventory WHERE model = {quote_model} AND count >= {count}""")
        #     return check
        check = self.mycursor.fetchall()
        print(check)

class TableEntry(Table):
    """Class for adding entries into tables within the epds database"""
    def __init__(self):
        mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'EPDS6425',
        database = 'epds_database'
        )
        self.mycursor = mydb.cursor(buffered=True)
        self.mydb = mydb

    def new_address(self, cust_code, billing = 'NULL', shipping = 'NULL', site = 'NULL'):
        """Adds a new address into the address table."""
        self.mycursor.execute(f"""INSERT INTO address (cust_code, billing, shipping, site)
VALUES ('{cust_code}', '{billing}', '{shipping}', '{site}');""")
        self.mydb.commit()

    def new_customer(self, name, cust_code):
        """Adds a new customer into the customer table."""
        self.mycursor.execute(f"""INSERT INTO customer (name, cust_code)
VALUES ('{name}', '{cust_code}')""")
        self.mydb.commit()

    def new_job(self, cust_code, name = 'NULL', desc = 'NULL'):
        """Adds a new job into the jobs table."""
        self.mycursor.execute(f"""INSERT INTO jobs (name, job_desc, cust_code)
VALUES ('{name}', '{desc}', '{cust_code}');""")
        self.mydb.commit()

    def new_poc(self, cust_code, name, phone, email):
        """Adds new point of contact to a customer"""
        self.mycursor.execute(f"""INSERT INTO poc (name, phone_num, email, cust_code)
VALUES ('{name}', '{phone}', '{email}', '{cust_code}')""")
        self.mydb.commit()

    def new_quote(self, quote_id, cust_code):
        """Adds quote to quote table."""
        self.mycursor.execute(f"""INSERT INTO quote (quote_id, cust_code)
VALUES ('{quote_id}', '{cust_code}')""")
        self.mydb.commit()

    def new_model(self, model, desc, warranty = 'NULL', unit_price = 'NULL',
                  taa = 'NULL', origin = 'NULL'):
        """Adds a new model into the model table."""
        self.mycursor.execute(
            f"""INSERT INTO model (model, info, warranty, unit_price, taa, country_of_origin)
VALUES('{model}', '{desc}', '{warranty}', '{unit_price}', '{taa}', '{origin}');""")
        self.mydb.commit()

    def new_mfr(self, name):
        """Adds a new mfr into the mfr table."""
        self.mycursor.execute(f"""INSERT INTO mfr (name)
VALUES('{name}');""")
        self.mydb.commit()

    def new_vendor(self, name):
        """Adds a new vendor into the vendor table."""
        self.mycursor.execute(f"""INSERT INTO vendors (name)
VALUES('{name}')""")
        self.mydb.commit()

test = Table()
test = TableEntry()

test.inventory_check('Colin', 1)