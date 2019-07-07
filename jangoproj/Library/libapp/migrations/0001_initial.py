# Generated by Django 2.2.3 on 2019-07-05 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Librarian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('contact', models.IntegerField()),
                ('salary', models.IntegerField()),
                ('mail', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'emp_data',
            },
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('landline', models.IntegerField()),
                ('librarian', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='libapp.Librarian')),
            ],
            options={
                'db_table': 'lib_data',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('issue_date', models.DateField()),
                ('library', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libapp.Library')),
            ],
        ),
    ]
