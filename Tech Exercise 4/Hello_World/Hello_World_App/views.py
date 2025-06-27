from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello EcoEats!")

# Create your views here.
def hello_EcoEats(request):
    return render(request, 'hello.html')

def hello_komlan(request):
	return HttpResponse("Hello from Komlan!")
