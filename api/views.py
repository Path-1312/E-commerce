from django.shortcuts import render
from django.shortcuts import HttpResponse

def index(request):
    return render(request, 'api/api.html')
