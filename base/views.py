from django.shortcuts import render
from blog.models import Post


def home(request):
	posts = Post.objects.all()
	context = {'posts':posts}
	return render(request, 'base/index.html', context)

def contact(request):
	return render(request, 'base/contact.html')