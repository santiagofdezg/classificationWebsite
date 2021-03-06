# Generated by Django 2.1.7 on 2019-04-16 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassificationAlgorithm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('enabled', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('enabled', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='ParameterizationAlgorithm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('enabled', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='SavedModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('accuracy', models.DecimalField(decimal_places=6, max_digits=7, null=True)),
                ('classif_alg', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='classifier.ClassificationAlgorithm')),
                ('dataset', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='classifier.Dataset')),
                ('param_alg', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='classifier.ParameterizationAlgorithm')),
            ],
        ),
    ]
