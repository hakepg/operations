from django.contrib import admin

# Register your models here.

from empapp.models import Employee

admin.site.register(Employee)