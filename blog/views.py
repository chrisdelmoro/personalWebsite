from django.shortcuts import render, get_object_or_404
from .models import Post, Category

def blog(request):
	posts = Post.objects.all()
	context = {'posts':posts}
	return render(request, 'blog/blog_home.html', context)

def detail(request, category_slug, slug):
	post = get_object_or_404(Post, slug=slug)
	context = {'post':post}
	return render(request, 'blog/detail.html', context)

def category(request, slug):
	category = get_object_or_404(Category, slug=slug)
	context = {'category':category}
	return render(request, 'blog/category.html', context)