from django.urls import path
from classifier.views import (
    classifier_view,
    # classification_results_view,
    # model_training_results_view
)

app_name = 'classifier'

urlpatterns = [
    path('', classifier_view, name='index'),
    # path('results/', classification_results_view, name='classification-results'),
    # path('model-training/', model_training_results_view, name='model-training-results')
]