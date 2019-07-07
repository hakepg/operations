from flaskproj.flask_rest_api_p5batch.producer.prod_service import *
from flask import request
import json


db.create_all()
strservice = prod_service()

@producer.route('/welcome/') #http://127.0.0.1:5001/welcome/
def welcome_to_producer():
    return 'producer invoked..!!'

@producer.route('/service/', methods = ['POST']) #http://127.0.0.1:5001/service
def save_student():
    reqjson = request.get_json()
    st = Student(**reqjson)
    return strservice.add_prod(st)

@producer.route('/service/', methods = ['PUT'])
def update_student():
    reqjson = request.get_json()
    stu = Student(**reqjson)
    return strservice.update_prod(stu)

@producer.route('/service/<int:sid>', methods=['DELETE'])
def delete_student(sid):
    return strservice.delete_prod(sid)

@producer.route('/service/<int:sid>', methods = ['GET'])
def get_student(sid):
    student = strservice.get_prod(sid)
    print(student.__dict__)


    stud_dict = {}
    # stud.__dict__.pop('perc')
    student.__dict__.pop('_sa_instance_state')
    # student.__dict__.pop('active')
    stud_dict[student.id] = student.__dict__
    return json.dumps(stud_dict)  # convert python object to json object

@producer.route('/service/',methods = ['GET'])
def get_all_student():
    allstud=strservice.get_all_prod()
    print(allstud)

    dictOfStuds = {}
    for st in allstud:
        st.__dict__.pop('_sa_instance_state')
        dictOfStuds[st.id] = st.__dict__
    return json.dumps(dictOfStuds)



if __name__ == '__main__':
    producer.run(debug = True,port=5001)


