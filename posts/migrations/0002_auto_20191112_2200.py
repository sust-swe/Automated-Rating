# Generated by Django 2.2.6 on 2019-11-12 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemslist',
            name='release_year',
            field=models.CharField(max_length=200),
        ),
    ]
