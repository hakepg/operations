from flask import Flask
from flask_sqlalchemy import SQLAlchemy

producer = Flask(__name__)

producer.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:agh123@localhost:3306/ppydb'
producer.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(producer)

class Student(db.Model):
    id = db.Column('stud_id',db.Integer,primary_key=True)
    name = db.Column('stud_name', db.String(100),nullable=False)
    age = db.Column('stud_age', db.Integer)
    city = db.Column('stud_city', db.String(100),nullable=False)
    # active = db.Column()
'''
'name':'ppp',
'age':26,
'city':'pune'
'''



