from django.http import HttpResponse

def home (request):
    return HttpResponse('<a href="files/index.html">Home</a>')
# Create your views here.