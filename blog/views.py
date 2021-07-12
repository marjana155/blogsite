from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Blogs, Category
# Create your views here.

categories = Category.objects.all()
'''def index(request):
    blogs = Blogs.objects.all()
    category = Category.objects.all()
    return render(request, 'home.html', {'blogs': blogs, 'categories': category})
'''


def detail(request, blog_id):
    b = Blogs.objects.get(id=blog_id)

    return render(request, 'detail.html', {'blog': b, 'categories': categories})


def category(request, blog_category):
    c = get_object_or_404(Category, title=blog_category)
    b = Blogs.objects.filter(category=c)
    return render(request, 'category.html', {'categories': categories, 'blogs': b})
