from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello EcoEats! From Sophia :)") #Changed this line here

# Create your views here.
def hello_EcoEats(request):
    return render(request, 'hello.html')
