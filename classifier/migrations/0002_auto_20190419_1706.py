# Generated by Django 2.1.7 on 2019-04-19 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classifier', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savedmodel',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]