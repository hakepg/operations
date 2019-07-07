from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:agh123@localhost:3306/cruddb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


cust_wait = db.Table('waiter_customer',
                     db.Column('cid', db.ForeignKey('waiter.wait_id'),primary_key = True),
                     db.Column('wid', db.ForeignKey('customer.cust_id'),primary_key = True)
                     )

class Place(db.Model): #this class is child of db.
    id = db.Column('pincode', db.Integer, primary_key = True)
    name = db.Column('place_name', db.String(50),nullable = False)
    city = db.Column('place_city', db.String(50),nullable = False)
    state = db.Column('place_state', db.String(50),nullable = False)
    restaurant = db.relationship('Restaurant',backref = 'places',uselist = False) # onetoone bet place and rest

# Place(name='katraj',city='pune',state='MH')


class Restaurant(db.Model): #this class is child of db.
    id = db.Column('rest_id', db.Integer, primary_key = True)
    name = db.Column('rest_name', db.String(100),nullable = False)
    type = db.Column('rest_type', db.String(100),nullable = False)
    owner = db.Column('rest_owner', db.String(100),nullable = False)
    pid = db.Column(db.Integer, db.ForeignKey('place.pincode'),nullable =False)
    waiter = db.relationship('Waiter', backref='restaurant', uselist = True) # for onetomany relationship bet restaurant and waiter ==> 1rest & many waiter
# Restaurant(name='barbiq',type='veg',owner='pgh')

class Waiter(db.Model): #this class is child of db.
    id = db.Column('wait_id', db.Integer, primary_key = True)
    name = db.Column('wait_name', db.String(100),nullable = False)
    age = db.Column('wait_age', db.Integer)
    salary = db.Column('wait_sal', db.Integer)
    rid = db.Column(db.Integer, db.ForeignKey('restaurant.rest_id'),nullable = False)
    customer = db.relationship('Customer', secondary = cust_wait, lazy = 'subquery',
                               backref = (db.backref('waiters', lazy = True)))
# Waiter(name='aaa',age=25,salary=2500)

class Customer(db.Model): #this class is child of db.
    id = db.Column('cust_id', db.Integer, primary_key = True)
    name = db.Column('cust_name', db.String(100),nullable = False)
    age = db.Column('cust_age', db.Integer)
    type = db.Column('cust_type', db.String(100),nullable = False)
# Customer(name='pratu',age=25,type='veg')
# db.create_all()
#path -E:\\python_my_practice\\flaskproj\\simpleCrud\\