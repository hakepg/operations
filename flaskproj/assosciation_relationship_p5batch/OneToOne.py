from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:agh123@localhost:3306/onedb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db = SQLAlchemy(app)

class Employee(db.Model): #this class is child of db.
    id = db.Column('emp_id', db.Integer, primary_key = True)
    name = db.Column('emp_name', db.String(100),nullable = False)
    age = db.Column('emp_age', db.Integer)
    salary = db.Column('emp_sal', db.Integer)
    company = db.relationship('Company', backref='employees', lazy=True, uselist=False)

class Company(db.Model):
    id = db.Column('comp_id', db.Integer, primary_key = True)
    name = db.Column('comp_name', db.String(100),nullable = False)
    address = db.Column('comp_addr', db.String(100),nullable = False)
    eid = db.Column(db.Integer, db.ForeignKey('employee.emp_id'),nullable = False) # here 4 column are present
#db.ForeignKey('employee.id') that time when id = db.Column('here not mention the table name then simply use the
# column name'db.Integer, primary_key = True)
# otherwise classname.tablename will use



# db.drop_all()
# import os
# os.getcwd()
# os.chdir('E:\\python_my_practice\\flaskproj\\assosciation_relationship_p5batch\\')
# from OneToOne import *
# db.create_all()
# e1 =Employee(name='pgh', age=25, salary=28000)
# e2 =Employee(name='agh', age=26, salary=20000)
# e3 =Employee(name='ggh', age=28, salary=26000)
# e4 =Employee(name='sgh', age=24, salary=27000)
# e5 =Employee(name='gsh', age=22, salary=29000)
# c1=Company(name='infy', address = 'pune1',eid=1)
# c2=Company(name='cogni', address = 'pun2')
# c3=Company(name='persi', address = 'pune3')
# c4=Company(name='tcs', address = 'pune4')

# db.session.add_all([e1,e2,e3,e4,e5])
# db.session.commit()
# db.session.add_all([c1,c2,c3,c4])
# db.session.commit()
