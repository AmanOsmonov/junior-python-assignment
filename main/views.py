from django.shortcuts import render
from .models import Kani


def index(request):


    a = Kani.objects.reverse()[:10]
    return render(request, 'main/index.html', {'a': a})
# Create your views here.
