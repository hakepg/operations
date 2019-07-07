from django.db import models

# Create your models here.
class Product(models.Model):  #appname_classname
    product_name = models.CharField(max_length=30)
    product_vendor = models.CharField(max_length=30)
    product_price = models.IntegerField()
    product_qty = models.IntegerField()
    product_descr= models.CharField(max_length=30)
    product_labal=models.CharField(max_length=30)
    #product_labal2 = models.CharField(max_length=30,default='ABC')

    class Meta:
        db_table= "product_info"