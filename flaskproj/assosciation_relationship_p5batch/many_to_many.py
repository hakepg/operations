from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:agh123@localhost:3306/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

stud_addr = db.Table('Student_address',
db.Column('sid', db.Integer, db.ForeignKey('student.Stud_id'),primary_key = True), #when table name given then use th name of table like student.stud_id
db.Column('aid', db.Integer, db.ForeignKey('address.pincode'),primary_key = True) #if not given then simply use classname.column name means variable name
)

class Student(db.Model):
    id = db.Column('Stud_id', db.Integer, primary_key = True)
    name = db.Column('Stud_name', db.String(50), nullable = False)
    age = db.Column('Stud_age', db.Integer)
    addresses = db.relationship('Address', secondary=stud_addr, lazy='subquery',
                           backref = db.backref('students', lazy=True))
    # subjects = db.relationship('Subject', secondary=stsj, lazy='subquery',
    #                            backref=db.backref('students', lazy=True))

# s1 = Student(name = 'Pratima', age = 25)

class Address(db.Model):
    pincode = db.Column('pincode', db.Integer, primary_key = True)
    city = db.Column('city_name', db.String(50), nullable=False)
    state = db.Column('state_name', db.String(50), nullable = False)

# ad1 = Address(city = 'pune', state = 'MH')
# os.chdir('E:\\python_my_practice\\flaskproj\\assosciation_relationship_p5batch\\')


