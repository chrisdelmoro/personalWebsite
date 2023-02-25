from django.http import HttpResponse

from django.shortcuts import render

from blog.models import Post


def home(request):
	posts = Post.objects.filter(status=Post.ACTIVE)
	context = {'posts':posts}
	return render(request, 'base/index.html', context)

def contact(request):
	return render(request, 'base/contact.html')

def robots_txt(request):
	text = [
		"User-Agent: *",
		"Disallow: /admin/",
	]
	return HttpResponse("\n".join(text), content_type="text/plain")