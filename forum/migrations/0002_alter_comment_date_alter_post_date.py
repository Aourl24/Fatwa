# Generated by Django 4.0.2 on 2022-06-05 17:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 5, 18, 24, 34, 368852)),
        ),
        migrations.AlterField(
            model_name='post',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 5, 18, 24, 34, 361900)),
        ),
    ]
