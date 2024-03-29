# Generated by Django 2.1 on 2019-06-14 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20190614_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='waiter',
            field=models.ManyToManyField(to='myapp.Waiter'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='owner',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='rating',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='type',
            field=models.CharField(max_length=20),
        ),
    ]
