from django.db import models

from ckeditor.fields import RichTextField


class Category(models.Model):
	title = models.CharField(max_length=255)
	slug = models.SlugField()

	class Meta:
		ordering = ('title',)
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return '/%s/' % self.slug

class Post(models.Model):
	ACTIVE = 'active'
	DRAFT = 'draft'

	CHOISE_STATUS = (
		(ACTIVE, 'Active'),
		(DRAFT, 'Draft')
	)

	category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
	title = models.CharField(max_length=255)
	slug = models.SlugField()
	intro = RichTextField()
	body = RichTextField()
	created_at = models.DateTimeField(auto_now_add = True)
	status = models.CharField(max_length=10, choices=CHOISE_STATUS, default=ACTIVE)

	class Meta:
		ordering = ('-created_at',)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return '/%s/%s/' % (self.category.slug, self.slug)