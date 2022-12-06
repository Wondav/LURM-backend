# Generated by Django 4.1.3 on 2022-12-06 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PastQuestion',
            fields=[
                ('courseCode', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('semester', models.CharField(choices=[('Alpha', 'Alpha'), ('Omega', 'Omega')], max_length=5)),
                ('session', models.CharField(max_length=10)),
                ('level', models.CharField(choices=[('100', '100'), ('200', '200'), ('300', '300'), ('400', '400'), ('500', '500')], max_length=3)),
                ('questionFile', models.FileField(upload_to='')),
            ],
        ),
    ]
