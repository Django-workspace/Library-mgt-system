# Generated by Django 4.0.6 on 2022-08-03 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='staff',
            field=models.BooleanField(default=False),
        ),
    ]
