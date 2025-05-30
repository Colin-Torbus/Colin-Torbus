import mysql.connector
from mysql.connector import Error
import pandas as pd
from typing import Optional


class TableEntry():
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

test = TableEntry()



class TableUpdate():
    """delete me later or make me useful ##FIXME"""

    def __init__(self):
        mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'EPDS6425',
        database = 'epds_database'
        )
        self.mycursor = mydb.cursor()
        self.mydb = mydb
   
    def table_update(self, table, ar1 = None, ar2 = None, ar3 = None, ar4 = None, ar5 = None):
        """maybe revisit ##FIXME"""
        ## FIXME may need different functions per table?
        params = [ar1, ar2, ar3, ar4, ar5]
        args = []
        for ar in params:
            if ar != None:
                args.append(params[ar])


        print(args)  
        val = f'{ar1}, {ar2}'

        self.mycursor.execute(sql, val)
        self.mydb.commit    
        print(self.mycursor.rowcount, 'record inserted')
