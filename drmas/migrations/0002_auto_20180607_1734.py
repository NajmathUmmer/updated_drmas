# Generated by Django 2.0.6 on 2018-06-07 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drmas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='age',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='sex',
            field=models.CharField(default='', max_length=10),
        ),
    ]
