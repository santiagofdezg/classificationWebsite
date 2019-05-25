from django.shortcuts import render,redirect

from .forms import (
    SearchForm
)

# Create your views here.

def search_view(request):
    if request.user.is_authenticated:
        template = 'search/index.html'
        if request.method == 'GET':
            context = {
                'form' : SearchForm()
            }
        else:
            form = SearchForm(request.POST)
            if form.is_valid():
                template = 'search/query_results.html'
                context = {
                    'data' : ''
                }
            else:
                context = {'form' : form}
        response = render(request, template, context)

    else:
        response = redirect('authentication:login')

    return response