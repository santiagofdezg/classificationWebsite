from django.urls import path, include


app_name = 'authentication'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
]

'''
URLs provided by auth:
    authentication/login/ [name='login']
    authentication/logout/ [name='logout']
    authentication/password_change/ [name='password_change']
    authentication/password_change/done/ [name='password_change_done']
    authentication/password_reset/ [name='password_reset']
    authentication/password_reset/done/ [name='password_reset_done']
    authentication/reset/<uidb64>/<token>/ [name='password_reset_confirm']
    authentication/reset/done/ [name='password_reset_complete']
'''