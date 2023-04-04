from django.db.models import Q

from django.shortcuts import render, get_object_or_404

from .models import Post, Category, PostImages

from taggit.models import Tag

from django.core.paginator import Paginator

def blog(request): # Blog's home page
	posts = Post.objects.filter(status=Post.ACTIVE)
	paginator = Paginator(posts, 2)

	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	category = Category.objects.all()
	context = {
		'page_obj':page_obj,
		'categories':category,
	}
	return render(request, 'blog/blog.html', context)

def detail(request, category_slug, slug): # Post's detail
	post = get_object_or_404(Post, slug=slug, status=Post.ACTIVE)
	images = post.images.all() # Images from the BODY of the post.
	tags = post.tags.all()
	context = {
		'post':post,
		'images':images,
		'tags':tags,
	}
	return render(request, 'blog/detail.html', context)

def category(request, slug): # Filter posts by category
	category = get_object_or_404(Category, slug=slug)
	posts = category.posts.filter(status=Post.ACTIVE)
	paginator = Paginator(posts, 2)

	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	context = {
		'category':category,
		'page_obj':page_obj,
	}
	return render(request, 'blog/category.html', context)

def tag(request, slug): # Filter posts by tags
	tag = get_object_or_404(Tag, slug=slug)
	posts = Post.objects.filter(tags=tag, status=Post.ACTIVE)
	paginator = Paginator(posts, 2)

	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	context = {
		'tag':tag,
		'page_obj':page_obj,
	}
	return render(request, 'blog/tag.html', context)

def search(request): # Search posts for term inside its title, intro or body
	query = request.GET.get('query', '')
	posts = Post.objects.filter(status=Post.ACTIVE).filter(Q(title__icontains=query) | Q(intro__icontains=query) | Q(body__icontains=query))
	paginator = Paginator(posts, 2)

	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	context = {
		'page_obj':page_obj,
		'query':query,
	}
	return render(request, 'blog/search.html', context)