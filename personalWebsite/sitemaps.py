from django.contrib.sitemaps import Sitemap

from django.shortcuts import reverse

from blog.models import Category, Post


class HomeSitemap(Sitemap):
	def items(self):
		return ['home']

	def location(self, item):
		return reverse(item)

class CategorySitemap(Sitemap):
	def items(self):
		return Category.objects.all()

class PostSitemap(Sitemap):
	def items(self):
		return Post.objects.filter(status=Post.ACTIVE)

	def lastmod(self, obj):
		return obj.created_at

class ContactSitemap(Sitemap):
	def items(self):
		return ['contact']

	def location(self, item):
		return reverse(item)