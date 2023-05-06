from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class homepage(TemplateView):
    template_name = 'home/index.html'

class characterArchive(TemplateView):
    template_name = 'home/characterarchive.html'
    
class locations(TemplateView):
    template_name = 'home/locations.html'