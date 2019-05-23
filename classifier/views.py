from django.shortcuts import render,redirect

from .models import (
    Dataset,
    ParameterizationAlgorithm,
    ClassificationAlgorithm,
    SavedModel
)
from .forms import (
    TrainedModelForm,
    TrainNewModelForm,
    TrainAllModelsForm
)
from .textclassifier.ClassifierModel import ClassifierModel

# Create your views here.

# def classifier_view(request,*args, **kwargs):
#     return render(request, 'classifier/index.html', {})

# class ClassifierView(View):
#     template_name = 'classifier/index.html'

def classifier_view(request):
    if request.user.is_authenticated:
        template = 'classifier/index.html'
        context = {}
        if request.method == 'POST':
            if request.POST['choice'] == 'trainedModel':
                formTrained = TrainedModelForm(request.POST)
                formNew = TrainNewModelForm()
                formAll = TrainAllModelsForm()
                if formTrained.is_valid():
                    template = 'classifier/classifier_classification_' \
                               'results.html'
                    db_model = formTrained.cleaned_data['savedModel']
                    text = formTrained.cleaned_data['textClassify']
                    topics = classify_text(db_model.param_alg.name,
                                           db_model.classif_alg.name,
                                           db_model.dataset.name, text)
                    context = {
                        'model': formTrained.cleaned_data['savedModel'],
                        'text': formTrained.cleaned_data['textClassify'],
                        'topics': ', '.join(topics)
                    }
                else:
                    context = {
                        'formTrained': formTrained,
                        'formNew': formNew,
                        'formAll': formAll
                    }
            elif request.POST['choice'] == 'newModel':
                formTrained = TrainedModelForm()
                formNew = TrainNewModelForm(request.POST)
                formAll = TrainAllModelsForm()
                if formNew.is_valid():
                    template = 'classifier/classifier_model_training_' \
                               'results.html'
                    param_alg = formNew.cleaned_data['param_alg']
                    classif_alg = formNew.cleaned_data['classif_alg']
                    dataset = formNew.cleaned_data['dataset']
                    percentage = formNew.cleaned_data['percentage']
                    # Training of the model
                    if (param_alg.name=='Doc2Vec' and
                        classif_alg.name=='NaiveBayes'):
                        context = {
                            'param_alg': param_alg.name,
                            'classif_alg': classif_alg.name,
                            'dataset': dataset.name,
                            'percentage': percentage,
                            'accuracy': 'This algorithms can not be trained '
                                        'together. Train another model.'
                        }
                    else:
                        accuracy = train_model(param_alg,classif_alg,dataset,
                                               percentage)
                        context = {
                            'param_alg': param_alg.name,
                            'classif_alg': classif_alg.name,
                            'dataset': dataset.name,
                            'percentage': percentage,
                            'accuracy': accuracy
                        }
                else:
                    context = {
                        'formTrained': formTrained,
                        'formNew': formNew,
                        'formAll': formAll
                    }
            elif request.POST['choice'] == 'trainAll':
                formTrained = TrainedModelForm()
                formNew = TrainNewModelForm()
                formAll = TrainAllModelsForm(request.POST)
                if formAll.is_valid():
                    template = 'classifier/classifier_all_models_results.html'
                    percentage = formAll.cleaned_data['percentage']
                    context = {
                        'model_list': train_all_models(percentage)
                    }
                else:
                    context = {
                        'formTrained': formTrained,
                        'formNew': formNew,
                        'formAll': formAll
                    }
            else:
                formTrained = TrainedModelForm()
                formNew = TrainNewModelForm()
                formAll = TrainAllModelsForm()
                context = {
                    'formTrained': formTrained,
                    'formNew': formNew,
                    'formAll': formAll
                }

        else:
            # When method = GET
            formTrained = TrainedModelForm()
            formNew = TrainNewModelForm()
            formAll = TrainAllModelsForm()
            context = {
                'formTrained': formTrained,
                'formNew': formNew,
                'formAll': formAll
            }
        response = render(request, template, context)
    else:
        response = redirect('authentication:login')

    return response

def train_all_models(percentage):
    param_alg_list = ParameterizationAlgorithm.objects.all()
    classifier_alg_list = ClassificationAlgorithm.objects.all()
    dataset_list = Dataset.objects.all()
    model_list = []

    for dataset in dataset_list:
        for param_alg in param_alg_list:
            for classif_alg in classifier_alg_list:
                if not (param_alg.name=='Doc2Vec' and classif_alg.name=='NaiveBayes'):
                    accuracy = train_model(param_alg, classif_alg, dataset,
                                           percentage)
                    model = {
                        'param_alg': param_alg.name,
                        'classif_alg': classif_alg.name,
                        'dataset': dataset.name,
                        'training_set': percentage,
                        'accuracy': accuracy
                    }
                    model_list.append(model)
    return model_list

def train_model(param_alg, classif_alg, dataset, percentage):
    # param_alg, classif_alg and dataset are objects from the database

    # Train the model
    if dataset is None:
        classifier = ClassifierModel(param_alg.name,classif_alg.name,
                                     train_size=percentage/100,
                                     saved_model=False)
    else:
        classifier = ClassifierModel(param_alg.name,classif_alg.name,
                                     dataset.name, train_size=percentage/100,
                                     saved_model=False)
    classifier.train()
    classifier.save_model()
    accuracy = classifier.get_accuracy()

    # Create or update (if it already exists) the model in the database
    SavedModel.objects.update_or_create(
        name=classifier.name, defaults={
            'accuracy': accuracy,
            'param_alg': param_alg,
            'classif_alg': classif_alg,
            'dataset': dataset
        })
    return accuracy


def classify_text(param_alg, classif_alg, dataset, text):
    classifier = ClassifierModel(param_alg,classif_alg,dataset,saved_model=True)
    result = classifier.classify([text])
    return result[0]

# class CourseDeleteView(CourseObjectMixin, View):
#     template_name = "courses/course_delete.html" # DetailView
#     def get(self, request, id=None, *args, **kwargs):
#         # GET method
#         context = {}
#         obj = self.get_object()
#         if obj is not None:
#             context['object'] = obj
#         return render(request, self.template_name, context)
#
#     def post(self, request, id=None,  *args, **kwargs):
#         # POST method
#         context = {}
#         obj = self.get_object()
#         if obj is not None:
#             obj.delete()
#             context['object'] = None
#             return redirect('/courses/')
#         return render(request, self.template_name, context)


# def classification_results_view(request,*args, **kwargs):
#     return render(request, 'classifier/classifier_classification_results.html',{})
#
# def model_training_results_view(request,*args, **kwargs):
#     return render(request, 'classifier/classifier_model_training_results.html',{})
