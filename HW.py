

import sqlite3


def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return connection

def create_products(connection,products):
    try:
        sql = '''INSERT INTO products 
        (product_title,price,quanity)
        VALUES (?,?,?)'''
        cursor = connection.cursor()
        cursor.execute(sql,products)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def update_products(connection, products):
    try:
        sql = '''UPDATE products SET quantity = ?
        WHERE id = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, products)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def update_products1(connection, products):
    try:
        sql = '''UPDATE products SET price = ?
        WHERE id = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, products)
        connection.commit()
    except sqlite3.Error as e:
        print(e)




def delete_products(connection, id):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, (id,))
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def select_all_products(connection):
    try:
        sql = '''SELECT * FROM products'''
        cursor = connection.cursor()
        cursor.execute(sql)

        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)

def select_products_products_that_cost_hundred_som(connection,price):
    try:
        sql = '''SELECT * FROM products WHERE price <= ? and quantity >?'''
        cursor = connection.cursor()
        cursor.execute(sql,(price,))

        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)




def search_products(connection):
    try:
        sql = '''SELECT * FROM products WHERE product_title LIKE '%Eclair%' '''
        cursor = connection.cursor()
        cursor.execute(sql)

        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)



data_base_name = 'hw.db'


def create_table(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)

''
sql_create_products_table = '''
CREATE TABLE PRODUCTS (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL,
price DOUBLE (10,2) NOT NULL DEFAULT 0.0,
quanity INTEGER (5) NOT NULL DEFAULT(0))
'''

db_connection = create_connection(data_base_name)
if db_connection is not None:
    print('CONNECTION SUCCESSEFULLY!')

#     # create_table(db_connection,sql_create_products_table)
# create_products(db_connection,("Eclair Balm",85.20,7))
# create_products(db_connection,("Eclair Elseve",90.90,1))
# create_products(db_connection, ("Eclair Evesu",150.99,100))
# create_products(db_connection,("Garnier Fructis Balm",230.11,17))
# create_products(db_connection,("La rossa hair balm",700.45,3))
# create_products(db_connection,('VISPA Hair Balm',100.44,91))
# create_products(db_connection,("Hair balm. Medicinal herbs",88.14,14))
# create_products(db_connection,("Balm Charm Professional",14.88,88))
# create_products(db_connection,("Head &Shoulders Shampoo",77.12,74))
# create_products(db_connection,("Shampoo Palmolive",100.00,75))
# create_products(db_connection,("Shampoo blue lock",74.55,855))
# create_products(db_connection,('SHAMTU Shampoo',675.00,4))
# create_products(db_connection,("dior soap",745.00,85))
# create_products(db_connection,("DG soap",77.55,8))
# create_products(db_connection,("Cream soap",78852.00,12))


# select_products_products_that_cost_hundred_som(db_connection,100,5)
# delete_products(db_connection,7)
# update_products1(db_connection, (77.14, 3))
# update_products(db_connection,(1,2))
# select_all_products(db_connection)
# search_products(db_connection)

db_connection.close()



print('Done!')
