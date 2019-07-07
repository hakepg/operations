from flask_wtf import FlaskForm
from wtforms import IntegerField, TextField, BooleanField, SubmitField, Form,StringField,PasswordField,validators


class StudentForm(FlaskForm):
    id = IntegerField('Student Id',)
    name = TextField('Stud Name', [validators.Required("Please enter your Name")])
    age = IntegerField('Student Age')
    city = StringField('Student City', [validators.Required("Please enter your Name")])
    submit = SubmitField('Send')