# Generated by Django 3.2 on 2021-06-04 15:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('task', models.TextField()),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2021, 6, 4, 15, 56, 58, 534839, tzinfo=utc), verbose_name='Time published')),
                ('cover', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
