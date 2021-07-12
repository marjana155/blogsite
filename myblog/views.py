from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blog.models import Blogs, Category


def home(request):
    blogs = Blogs.objects.all()
    category = Category.objects.all()
    return render(request, 'home.html', {'blogs': blogs, 'categories': category})

