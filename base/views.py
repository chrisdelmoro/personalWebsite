from django.http import HttpResponse

from django.shortcuts import render

from blog.models import Post


def home(request):
	posts = Post.objects.filter(status=Post.ACTIVE)
	posts = posts[0:2]
	context = {'posts':posts}
	return render(request, 'base/home.html', context)

def robots_txt(request):
	text = [
		"User-Agent: *",
		"Disallow: /admin/",
	]
	return HttpResponse("\n".join(text), content_type="text/plain")