# Generated by Django 4.0.2 on 2022-05-19 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0010_alter_question_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='Support',
            field=models.ManyToManyField(blank=True, null=True, related_name='support', to='ask.Profile'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='dislike',
            field=models.ManyToManyField(blank=True, null=True, related_name='dislike', to='ask.Profile'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='like',
            field=models.ManyToManyField(blank=True, null=True, related_name='like', to='ask.Profile'),
        ),
    ]