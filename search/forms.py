#Change forms: https://docs.djangoproject.com/en/2.2/topics/forms/#rendering-fields-manually

from django import forms

from .searchengine.searchengine.search import Connection,Search

time_intervals = {
    'today': 'Today', 'week':'This week', 'month':'This month',
    '3months':'Last 3 months', 'year':'This year'
}
maximum_articles = [10, 15, 20, 30, 40]


class SearchForm(forms.Form):

    # Get the lists of categories and sources
    connection = Connection.get_connection()
    search = Search(connection, 'news')
    categories = search.get_all_categories()
    sources = search.get_all_sources()

    searchBar = forms.CharField(
                    widget=forms.TextInput(attrs={
                        'class' : 'form-control rounded-pill',
                        'id' : 'searchBar',
                        'name' : 'searchBar',
                        'minlenght' : 2,
                        'maxlenght' : 100,
                        'placeholder' : 'Between 2 and 100 characters.'
                    }))
    category = forms.ChoiceField(
                    widget=forms.Select(attrs={
                        'class' : 'form-control rounded-pill',
                        'id' : 'category',
                        'name' : 'category',
                    }),
                    choices = [('All','All')]+[(c,c) for c in categories]
                    )
    source = forms.ChoiceField(
                    widget=forms.Select(attrs={
                        'class' : 'form-control rounded-pill',
                        'id' : 'source',
                        'name' : 'source',
                    }),
                    choices = [('All','All')]+[(s,s) for s in sources]
                    )
    timeInterval = forms.ChoiceField(
                    widget=forms.Select(attrs={
                        'class' : 'form-control rounded-pill',
                        'name' : 'timeInterval',
                         'id' : 'timeInterval'
                    }),
                    choices = [(k,v) for k,v in time_intervals.items()]
                    )

    maxArticles = forms.ChoiceField(
                    widget=forms.Select(attrs={
                        'class' : 'form-control rounded-pill',
                        'name': 'maxArticles',
                        'id': 'maxArticles'
                    }),
                    choices = [(e,e) for e in maximum_articles]
                    )
