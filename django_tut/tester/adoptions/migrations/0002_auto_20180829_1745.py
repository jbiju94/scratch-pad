# Generated by Django 2.1 on 2018-08-29 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoptions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='submission_date',
            field=models.DateTimeField(),
        ),
    ]