# Generated by Django 4.0 on 2021-12-08 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_personalquestionunit_point'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='point',
            field=models.IntegerField(default=1),
        ),
    ]