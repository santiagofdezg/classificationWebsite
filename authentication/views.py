
from django.shortcuts import redirect

# Create your views here.
def home_view(request):
    if request.user.is_authenticated:
        response = redirect('classifier:index')
    else:
        response = redirect('authentication:login')
    return response