# Generated by Django 2.1.7 on 2019-06-14 16:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20190614_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 6, 14, 18, 20, 32, 723026)),
        ),
    ]
