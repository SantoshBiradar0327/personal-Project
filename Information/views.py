from django.shortcuts import render
from .models import Info

# Create your views here.
def home(request):
    Variable = Info.objects.all()
    return render(request, 'Information/home.html', {'anything':Variable})

def all_blogs(request):
    return render(request, 'Information/all_blogs.html')

def detail(request, blog_id):
    return render(request, 'Information/detail.html', {'id':blog_id})