# Generated by Django 4.0.2 on 2022-05-21 12:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0010_alter_comment_date_alter_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 21, 13, 41, 41, 5913)),
        ),
        migrations.AlterField(
            model_name='post',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 21, 13, 41, 40, 999604)),
        ),
    ]