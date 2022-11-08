from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def blog(request):
    a = Blog.objects.order_by('-date')[:4]
    return render(request, 'BLOG/all_blogs.html', {'bLoG':a})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'BLOG/detail.html', {'blog':blog})
