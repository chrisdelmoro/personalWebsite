from django.conf import settings

from django.http import FileResponse, HttpRequest, HttpResponse

from django.shortcuts import render

from blog.models import Post

from django.views.decorators.cache import cache_control
from django.views.decorators.http import require_GET

def home(request):
	posts = Post.objects.filter(status=Post.ACTIVE)
	posts = posts[0:2]
	context = {'page_obj':posts}
	return render(request, 'base/home.html', context)

@require_GET
@cache_control(max_age=60 * 60 * 24, immutable=True, public=True)  # one day
def favicon_file(request: HttpRequest) -> HttpResponse:
    name = request.path.lstrip("/")
    file = (settings.BASE_DIR / "static/images" / name).open("rb")
    return FileResponse(file)

@require_GET
@cache_control(max_age=60 * 60 * 24, immutable=True, public=True)  # one day
def web_manifest_files(request: HttpRequest) -> HttpResponse:
    name = request.path.lstrip("/")
    file = (settings.BASE_DIR / "static/manifest" / name).open("rb")
    return FileResponse(file)

def robots_txt(request):
	text = [
		"User-Agent: *",
		"Disallow: /admin/",
		"Disallow: /contact/success/",
	]
	return HttpResponse("\n".join(text), content_type="text/plain")