# Generated by Django 2.1 on 2019-07-04 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Age', models.IntegerField()),
                ('Salary', models.IntegerField()),
            ],
            options={
                'db_table': 'Emp_info',
            },
        ),
    ]
