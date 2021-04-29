from django.shortcuts import render

# Create your views here.


def home(request):
	return render(request,'html/home.html')

def index(request):
	return render(request,'html/index.html')