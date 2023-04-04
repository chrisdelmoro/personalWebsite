from django.db import models

from ckeditor.fields import RichTextField

from taggit.managers import TaggableManager


class Category(models.Model): # One-to-Many relation with Post
	title = models.CharField(max_length=255)
	slug = models.SlugField()

	class Meta:
		ordering = ('title',)
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return '/%s/' % self.slug


def post_header_path(instance, filename): # Used to specify save location of post header_img
	return '{0}/{1}'.format(instance.category.title + '/' + instance.title, filename)

class Post(models.Model):
	ACTIVE = 'active'
	DRAFT = 'draft'

	CHOISE_STATUS = (
		(ACTIVE, 'Active'),
		(DRAFT, 'Draft')
	)

	category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
	tags = TaggableManager() # Implemented with the taggit app
	title = models.CharField(max_length=255)
	title_tag = models.CharField(max_length=255) # Text displayed on HTML <title> tag
	slug = models.SlugField()
	header_img = models.ImageField(blank=True, null=True, upload_to=post_header_path) # Only the image displayed on the post header
	intro = RichTextField() # Rich text field from ckeditor
	body = RichTextField() # Rich text field from ckeditor
	created_at = models.DateTimeField(auto_now_add = True)
	status = models.CharField(max_length=10, choices=CHOISE_STATUS, default=ACTIVE)

	class Meta:
		ordering = ('-created_at',)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return '/%s/%s/' % (self.category.slug, self.slug)


def post_images_path(instance, filename): # Used to specify save location of post body images
	return '{0}/{1}'.format(instance.post.category.title + '/' + instance.post.title, filename)

class PostImages(models.Model): # Many-to-One relation with Post
	post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)
	image = models.ImageField(blank=True, null=True, upload_to=post_images_path)

	class Meta:
		verbose_name_plural = 'Post Images'

	def __str__(self):
		return self.post.title