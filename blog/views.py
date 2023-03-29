from django.db.models import Q

from django.shortcuts import render, get_object_or_404

from .models import Post, Category, PostImages

from taggit.models import Tag

def blog(request):
	posts = Post.objects.filter(status=Post.ACTIVE)
	category = Category.objects.all()
	context = {
		'posts':posts,
		'categories':category,
	}
	return render(request, 'blog/blog.html', context)

def detail(request, category_slug, slug):
	post = get_object_or_404(Post, slug=slug, status=Post.ACTIVE)
	images = post.images.all()
	tags = post.tags.all()
	context = {
		'post':post,
		'images':images,
		'tags':tags,
	}
	return render(request, 'blog/detail.html', context)

def category(request, slug):
	category = get_object_or_404(Category, slug=slug)
	posts = category.posts.filter(status=Post.ACTIVE)
	context = {
		'category':category,
		'posts':posts,
	}
	return render(request, 'blog/category.html', context)

def tag(request, slug):
	tag = get_object_or_404(Tag, slug=slug)
	posts = Post.objects.filter(tags=tag, status=Post.ACTIVE)
	context = {
		'tag':tag,
		'posts':posts,
	}
	return render(request, 'blog/tag.html', context)

def search(request):
	query = request.GET.get('query', '')
	posts = Post.objects.filter(status=Post.ACTIVE).filter(Q(title__icontains=query) | Q(intro__icontains=query) | Q(body__icontains=query))
	context = {
		'posts':posts,
		'query':query,
	}
	return render(request, 'blog/search.html', context)