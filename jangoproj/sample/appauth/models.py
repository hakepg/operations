from django.db import models
# from django.db.models.signals import pre_save

# Create your models here.

class Sample(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'sample_info'
