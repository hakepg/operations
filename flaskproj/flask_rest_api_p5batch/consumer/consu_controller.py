from flaskproj.flask_rest_api_p5batch.consumer.Rest_Api_consumer import *
from flask import Flask,request,render_template
from flaskproj.flask_rest_api_p5batch.consumer.consumer_form import StudentForm

consumer = Flask(__name__)
consumer.config['SECRET_KEY']='ASDHJA393JSAKSAJ839985JKSK'

# consumer.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:agh123@localhost:3306/cpydb'
# consumer.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(consumer)

@consumer.route('/client/')
def landing_page():
    return render_template('student.html',sform=StudentForm())

@consumer.route('/client/',methods =['POST'])
def save_into_student_form():
    print(request.form)

    st = Student(sid=request.form('Student Id'),
                 sname=request.form('Student Name'),
                 sage=request.form('Student Age'),
                 scity=request.form('Student City'))
    print(st)
    return render_template('student.html',sform=StudentForm())

if __name__ == '__main__':
    consumer.run(debug=True, port=5000)