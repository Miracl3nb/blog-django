from django.http import HttpResponse
from django.shortcuts import render
from .models import Project
# Create your views here.
def portfolio(request):
    projects =Project.objects.all()
    return render(request, 'portfolio.html', {'projects':projects})



