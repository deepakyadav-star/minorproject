# Generated by Django 3.1 on 2020-08-13 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=500)),
                ('qn', models.CharField(max_length=500)),
                ('op1', models.CharField(max_length=500)),
                ('op2', models.CharField(max_length=500)),
                ('op3', models.CharField(max_length=500)),
                ('op4', models.CharField(max_length=500)),
                ('ans', models.IntegerField()),
                ('level', models.IntegerField(default=1)),
            ],
        ),
    ]