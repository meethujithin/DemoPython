# Generated by Django 4.1.4 on 2022-12-12 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1993-03-22'),
            preserve_default=False,
        ),
    ]
