# Generated by Django 3.2 on 2021-06-04 17:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 4, 17, 39, 20, 724212, tzinfo=utc), verbose_name='Time published'),
        ),
    ]
