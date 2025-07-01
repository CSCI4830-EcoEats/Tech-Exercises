from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello EcoEats! This is Aristide, This is Komlan, From Sophia :)")
# Create your views here.
def hello_EcoEats(request):
    return render(request, 'hello.html')=

# def hello_world(request):
    # return HttpResponse("Hello EcoEats! This is Komlan.")

# Create your views here.
# def hello_EcoEats(request):
    # return render(request, 'hello.html')

# def hello_komlan(request):
	# return HttpResponse("Hello from Komlan!")