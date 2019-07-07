import pymysql
connection = None
def get_db_connection():
    global connection
    if connection==None:
        connection=pymysql.connect('localhost','root','root','basic')
        print('creating new connection with database')
    print('using same connection')
    return connection

CREATE_TABLE_SQL='''
            CREATE TABLE product_info( 
            product_id int NOT NULL,
            product_name char(50) NOT NULL, 
            product_price float,
            product_vendor char(50),
            product_category char(10),
            CONSTRAINT product_pk PRIMARY KEY (product_id))
            '''
INSERT_INTO_TABLE = ''' insert into product_info values(1,'pgh',5626,'Flipcart','A')

'''
DROP_TABLE_SQL = 'DROP TABLE PRODUCT_INFO'

def drop_table_from_database():
    connection=get_db_connection()
    channel=connection.cursor()
    channel.execute(DROP_TABLE_SQL)
    connection.commit()
# drop_table_from_database()
# print('drop tables from database successfully')

def create_table_into_db():
    connection=get_db_connection()
    channel=connection.cursor()
    channel.execute(CREATE_TABLE_SQL)
    connection.commit()
create_table_into_db()
print('product info table created successfully')

def insert_data_into_table():
    connection=get_db_connection()
    channel=connection.cursor()
    channel.execute(INSERT_INTO_TABLE)
    connection.commit()
insert_data_into_table()
print('data inserted into table successfully')


# connection=get_db_connection()
# channel=connection.cursor()
# channel.execute(CREATE_TABLE_SQL)
# connection.commit()
