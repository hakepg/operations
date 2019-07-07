from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:agh123@localhost:3306/otmdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Company(db.Model):
    id = db.Column('comp_id', db.Integer, primary_key = True)
    name = db.Column('comp_name', db.String(100),nullable = False)
    address = db.Column('comp_addr', db.String(100),nullable = False)
    employee = db.relationship('Employee',backref = 'comp',lazy = True, uselist =True)

# co1 = Company(name='infy', address='pune1')

class Employee(db.Model): #this class is child of db.
    id = db.Column('emp_id', db.Integer, primary_key = True)
    name = db.Column('emp_name', db.String(100),nullable = False)
    age = db.Column('emp_age', db.Integer)
    salary = db.Column('emp_sal', db.Integer)
    cid = db.Column(db.Integer, db.ForeignKey('company.comp_id'), nullable = False)

# emp1 =Employee(name='pgh', age=25, salary=28000)
db.create_all()