# Generated by Django 4.0.2 on 2022-05-30 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0015_question_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='mode',
            field=models.CharField(choices=[('Light', 'Light'), ('Dark', 'Dark')], default='Light', max_length=10),
        ),
    ]
