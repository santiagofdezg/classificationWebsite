from django.urls import path

from search.views import (
    search_view,
    article_view
)

app_name = 'search'

urlpatterns = [
    path('', search_view, name='index'),
    path('<str:id>', article_view, name='article')
    # path('results/', classification_results_view, name='classification-results'),
    # path('model-training/', model_training_results_view, name='model-training-results')
]