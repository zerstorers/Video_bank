# Generated by Django 3.0.3 on 2020-03-03 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_auto_20200228_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviesrent',
            name='date_return',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
