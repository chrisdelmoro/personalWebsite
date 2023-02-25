from django.db.models import Q

from django.shortcuts import render, get_object_or_404

from .models import Post, Category

def blog(request):
	posts = Post.objects.filter(status=Post.ACTIVE)
	category = Category.objects.all()
	context = {'posts':posts, 'categories':category}
	return render(request, 'blog/index.html', context)

def detail(request, category_slug, slug):
	post = get_object_or_404(Post, slug=slug, status=Post.ACTIVE)
	context = {'post':post}
	return render(request, 'blog/detail.html', context)

def category(request, slug):
	category = get_object_or_404(Category, slug=slug)
	posts = category.posts.filter(status=Post.ACTIVE)
	context = {'category':category, 'posts':posts}
	return render(request, 'blog/category.html', context)

def search(request):
	query = request.GET.get('query', '')
	posts = Post.objects.filter(status=Post.ACTIVE).filter(Q(title__icontains=query) | Q(intro__icontains=query) | Q(body__icontains=query))
	context = {'posts':posts, 'query':query}
	return render(request, 'blog/search.html', context)