# Generated by Django 4.2.2 on 2023-07-01 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydayapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1994-12-06'),
            preserve_default=False,
        ),
    ]
