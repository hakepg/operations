from django.db import models

# Create your models here.
class Employee(models.Model):
    Name = models.CharField(max_length=100)
    Age = models.IntegerField()
    Salary = models.IntegerField()

    class Meta:
        db_table = 'Emp_info'

# e1 = Employee(Name='Pratima', Age=25, Salary=457855)