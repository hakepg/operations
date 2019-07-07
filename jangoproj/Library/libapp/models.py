from django.db import models

# Create your models here.

class Librarian(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    contact = models.IntegerField()
    salary=models.IntegerField()
    mail=models.EmailField()

    class Meta:
        db_table='emp_data'

# Librarian(name='ppp',age=35,contact=9955566332,salary=545788,mail='pratima@gmail.com')


class Library(models.Model):
    name = models.CharField(max_length=50)
    landline = models.IntegerField()
    librarian = models.OneToOneField(Librarian,on_delete=models.CASCADE,primary_key=True)

    class Meta:
        db_table='lib_data'

# Library(name='central',landline=41258,librarian=lib) lib is object of librarian

class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    issue_date = models.DateField()
    library = models.ForeignKey(Library,on_delete=models.CASCADE)

    class Meta:
        db_table='book_data'

# Book(name='python2',author='pratima',issue_date='17/06/1994',library=l1)


class Student(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    contact=models.IntegerField()
    books=models.ManyToManyField(Book)

    class Meta:
        db_table='stud_data'

# Student(name='pgh',age=22,contact=45789)