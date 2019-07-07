from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']='pymysql+mysql://root:agh123@localhost:3306/flaskdb'
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:agh123@localhost:3306/flaskdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class Hotel(db.Model):
    hid = db.Column('hotel_id',db.Integer(),primary_key =True)
    hname = db.Column('hotel_name',db.String(200))
    htype = db.Column('hotel_type',db.String(100))
    address = db.relationship('Place',backref='hotel',uselist=False)

class Address(db.Model):
    aid = db.Column('aid', db.Integer(), primary_key=True)
    pin = db.Column('pincode', db.Integer())
    city = db.Column('city', db.String(200))
    hot_id = db.Column('hot_id',db.Integer(),db.ForeignKey('hotel.hotel_id'),nullable=False)


