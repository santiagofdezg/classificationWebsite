from django.contrib import admin

# Register your models here.
from .models import (
    Dataset,
    ParameterizationAlgorithm,
    ClassificationAlgorithm,
    SavedModel
)

admin.site.register(Dataset)
admin.site.register(ParameterizationAlgorithm)
admin.site.register(ClassificationAlgorithm)
admin.site.register(SavedModel)