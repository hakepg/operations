
# Generated by Django 2.1 on 2019-06-14 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='waiter',
            field=models.ManyToManyField(to='myapp.Waiter'),
        ),
    ]
