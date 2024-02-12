from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')
def home(request):
    return render(request,'home.html')
def firstpage(request):
    return render(request,'firstpage.html')
def contact(request):
    return render(request,'contact.html')
def deals(request):
    return render(request,'deals.html')
def archived(request):
    return render(request,'archive.html')
