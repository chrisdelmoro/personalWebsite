from django.shortcuts import render, get_object_or_404
from .models import Post

def blog(request):
	posts = Post.objects.all()
	context = {'posts':posts}
	return render(request, 'blog/home.html', context)

def detail(request, slug):
	post = get_object_or_404(Post, slug=slug)
	context = {'post':post}
	return render(request, 'blog/detail.html', context)