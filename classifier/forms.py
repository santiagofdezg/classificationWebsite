#Change forms: https://docs.djangoproject.com/en/2.2/topics/forms/#rendering-fields-manually

from django import forms
from .models import (
    SavedModel,
    ParameterizationAlgorithm,
    ClassificationAlgorithm,
    Dataset
)

class SavedModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name


class TrainedModelForm(forms.Form):
    min_lenght = '150'
    max_lenght = '3000'
    initial_choice = 'trainedModel'

    # Error message keys: required, invalid_choice
    savedModel = SavedModelChoiceField(
                        queryset=SavedModel.objects.all(),
                        to_field_name="name",
                        empty_label="-- Choose a model --",
                        widget=forms.Select(attrs={
                            'class' : 'form-control rounded-pill',
                            'name' : 'savedModel',
                             'id' : 'savedModel'
                        }))

    textClassify = forms.CharField(
                        widget=forms.Textarea(attrs={
                            'class' : 'form-control',
                            'id' : 'textClassify',
                            'name' : 'textClassify',
                            'rows' : "5",
                            'minlenght' : min_lenght,
                            'maxlenght' : max_lenght,
                            'placeholder' : 'Between 150 and 3000 characters. '
                                            'Only texts in English.'
                        }))

    choice = forms.CharField(
                        widget=forms.HiddenInput(attrs={
                            'name' : 'choice',
                            'id' : 'trainedModel',
                            'value' : 'trainedModel',

                        })
    )

    def clean_textClassify(self):
        text = self.cleaned_data.get('textClassify')
        if not (int(self.min_lenght) <= len(text) <= int(self.max_lenght)):
            raise forms.ValidationError('The text must contain between 150 '
                                        'and 3000 characters')
        return text

    # def clean_choice(self):
    #     print('oalaaaaa')
    #     if self.initial_choice != self.cleaned_data.get('choice'):
    #         raise forms.ValidationError('Son distintos')
    #     return self.cleaned_data.get('choice')


class TrainNewModelForm(forms.Form):
    min_percentage = 1
    max_percentage = 99

    dataset = SavedModelChoiceField(
                        queryset=Dataset.objects.all(),
                        to_field_name="name",
                        empty_label="-- Dataset --",
                        widget=forms.Select(attrs={
                            'class' : 'form-control rounded-pill',
                            'name' : 'newModelDataset',
                             'id' : 'newModelDataset'
                        }))

    param_alg = SavedModelChoiceField(
                        queryset=ParameterizationAlgorithm.objects.all(),
                        to_field_name="name",
                        empty_label="-- Parameterization Algorithm --",
                        widget=forms.Select(attrs={
                            'class' : 'form-control rounded-pill',
                            'name' : 'newModelParam',
                             'id' : 'newModelParam'
                        }))

    classif_alg = SavedModelChoiceField(
                        queryset=ClassificationAlgorithm.objects.all(),
                        to_field_name="name",
                        empty_label="-- Classification Algorithm --",
                        widget=forms.Select(attrs={
                            'class' : 'form-control rounded-pill',
                            'name' : 'newModelClassif',
                             'id' : 'newModelClassif'
                        }))

    percentage = forms.IntegerField(
                        widget=forms.NumberInput(attrs={
                            'id' : 'newModelPercent',
                            'name' : 'newModelPercent',
                            'max_value' : max_percentage,
                            'min_value' : min_percentage,
                            'value' : '70',
                        }))


    choice = forms.CharField(
                        widget=forms.HiddenInput(attrs={
                            'name' : 'choice',
                            'id' : 'newModel',
                            'value' : 'newModel'
                        }))

    def clean_percentage(self):
        percentage = self.cleaned_data.get('percentage')
        if not (self.min_percentage <= percentage <= self.max_percentage):
            raise forms.ValidationError('The size of the training set must '
                                        'be a value between 1% and 99%')
        return percentage


class TrainAllModelsForm(forms.Form):
    min_percentage = 1
    max_percentage = 99

    dataset = SavedModelChoiceField(
                        queryset=Dataset.objects.all(),
                        to_field_name="name",
                        empty_label="-- Dataset --",
                        widget=forms.Select(attrs={
                            'class': 'form-control rounded-pill',
                            'name': 'trainAllDataset',
                            'id': 'trainAllDataset',
                        }))

    percentage = forms.IntegerField(
                        widget=forms.NumberInput(attrs={
                            'id': 'trainAllPercent',
                            'name': 'trainAllPercent',
                            'max_value': max_percentage,
                            'min_value': min_percentage,
                            'value': '70',
                        }))

    choice = forms.CharField(
                        widget=forms.HiddenInput(attrs={
                            'name': 'choice',
                            'id': 'trainAll',
                            'value': 'trainAll',
                        }))

    def clean_percentage(self):
        percentage = self.cleaned_data.get('percentage')
        if not (self.min_percentage <= percentage <= self.max_percentage):
            raise forms.ValidationError('The size of the training set must '
                                        'be a value between 1% and 99%')
        return percentage

