import pymysql

from flaskproj.flask_demo_app_sqlquery.empinfo import Employee

def getConnection():
    connection = pymysql.connect('localhost','root','agh123','ppydb')
    return connection

def create_table():
    CREATE_TABLE_SQL = '''create table employee_info (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        empName varchar(20),
                        empAge varchar(30),
                        empSal float
                    
                        )'''

    connection = getConnection()
    cursor =connection.cursor()
    cursor.execute(CREATE_TABLE_SQL)
    connection.commit()

def get_all_empinfo():
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute('select * from employee_info')
    resultset = cursor.fetchall()
    print(resultset)
    listofemps=[]
    for row in resultset:
        e1 = Employee(eid=row[0], ename=row[1], eage=row[2], esal=row[3])
        listofemps.append(e1)
    return listofemps

def create_employee_records(emp):
    INSERT_QUERY = 'INSERT INTO EMPLOYEE_INFO VALUES({},{},\'{}\',{})'.format(
        emp.empId,emp.empName,emp.empAge,emp.empSal
    )
    print(INSERT_QUERY)
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute(INSERT_QUERY)
    connection.commit()


