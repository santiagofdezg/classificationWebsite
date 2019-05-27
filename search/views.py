from django.shortcuts import render,redirect
from elasticsearch import NotFoundError
from django.views.defaults import page_not_found

from .forms import (
    SearchForm
)
from .searchengine.search import Connection, Search, Index

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
                text = form.cleaned_data['searchBar']
                category = form.cleaned_data['category']
                source = form.cleaned_data['source']
                time_interval = form.cleaned_data['timeInterval']
                max_articles = form.cleaned_data['maxArticles']

                connection = Connection.get_connection()
                search = Search(connection, 'news')
                articles = search.search_news(text, category,source,
                                              time_interval, max_articles)
                context = {
                    'articles' : articles
                }
            else:
                context = {'form' : form}
        response = render(request, template, context)

    else:
        response = redirect('authentication:login')

    return response


def article_view(request, id):
    if request.user.is_authenticated:
        template = 'search/article_view.html'

        connection = Connection.get_connection()
        search = Search(connection, 'news')
        try:
            article = search.search_by_id(id)
            context = {
                'title': article.title,
                'text': article.article,
                'category': article.category,
                'author': article.author,
                'date': article.date,
                'source': article.source
            }
            response = render(request, template, context)
        except NotFoundError:
            return page_not_found()
    else:
        response = redirect('authentication:login')

    return response