from django.db import models
from django.urls import reverse

# Create your models here.
class Dataset(models.Model):
    name = models.CharField(max_length=100, unique=True)
    enabled = models.IntegerField(default=1)

class ParameterizationAlgorithm(models.Model):
    name = models.CharField(max_length=100, unique=True)
    enabled = models.IntegerField(default=1)

class ClassificationAlgorithm(models.Model):
    name = models.CharField(max_length=100, unique=True)
    enabled = models.IntegerField(default=1)

class SavedModel(models.Model):
    name = models.CharField(max_length=200, unique=True)
    param_alg = models.ForeignKey(ParameterizationAlgorithm,
                                  on_delete=models.SET_NULL,null=True)
    classif_alg = models.ForeignKey(ClassificationAlgorithm,
                                    on_delete=models.SET_NULL, null=True)
    dataset = models.ForeignKey(Dataset, on_delete=models.SET_NULL, null=True)
    accuracy = models.DecimalField(decimal_places=6, max_digits=7, null=True)

