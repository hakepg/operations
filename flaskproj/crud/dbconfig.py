from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__,template_folder='templates')

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:agh123@localhost:3306/scp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)