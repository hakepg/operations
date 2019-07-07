import requests
from flaskproj.flask_rest_api_p5batch.consumer.consu_controller import *

BASE_URI = 'http://127.0.0.1:5001/service/'

class Student:
    def __init__(self,sid,sname,sage,scity):
        self.id = sid
        self.name = sname
        self.age= sage
        self.city = scity

    def __str__(self):
        return f'{self.__dict__}'

    def __repr__(self):
        return str(self)

def get_all_data_from_producer():
    response = requests.get(BASE_URI)
    # print(response.json())
    # '1': {'name': 'hdsjfra', 'id': 1, 'city': 'Pune1', 'age': 24},
    resjson=response.json()
    print(type(resjson))
    print(resjson)
    listofstud =[]
    for value in resjson.values():
        st = Student(sid=value.get('id'),
                     snmae=value.get('name'),
                     sage=value.get('age'),
                     scity=value.get('city'))
        listofstud.append(st)
    print(listofstud)


def get_single_data_from_producer(sid):
    response = requests.get(BASE_URI+str(sid))
    resjson=response.json()
    print(type(resjson))
    print(response.status_code)

def delete_single_data_from_producer(sid):
    response = requests.delete(BASE_URI+str(sid))
    print(response.text)
    print(response.status_code)

def insert_data_into_producer(stud):
    response = requests.post(BASE_URI,json=stud.__dict__)
    print(response.text)
    print(response.status_code)


def update_data_into_producer(stud):
    response = requests.put(BASE_URI,json=stud)
    print(response.text)

dictValue = {'id':7,'name':'atul','age':25,'city':'pune44'}
# get_all_data_from_producer()
# get_single_data_from_producer(3)
# delete_single_data_from_producer(7)
insert_data_into_producer(save_into_student_form)
# update_data_into_producer(dictValue)