# Generated by Django 4.0 on 2021-12-08 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filterquestion',
            name='cur_answer',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='personalquestion',
            name='cur_answer',
            field=models.TextField(default=None),
        ),
    ]
