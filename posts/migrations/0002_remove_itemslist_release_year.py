# Generated by Django 2.2.6 on 2019-11-12 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemslist',
            name='release_year',
        ),
    ]
