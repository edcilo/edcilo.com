# Generated by Django 3.1.7 on 2021-03-10 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0002_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='landing',
            name='domain',
            field=models.CharField(default='127.0.0.1;localhost', max_length=100),
        ),
    ]
