from django.contrib import admin

from .models import Post, Category, PostImages

class PostImagesAdmin(admin.StackedInline):
	model = PostImages

class PostAdmin(admin.ModelAdmin):
	search_fields = ['title', 'intro', 'body']
	list_display = ['title', 'slug', 'category', 'created_at', 'status']
	list_filter = ['category', 'created_at', 'status']
	prepopulated_fields = {'slug':('title',)}
	inlines = [PostImagesAdmin, ]

class CategoryAdmin(admin.ModelAdmin):
	search_fields = ['title']
	list_display = ['title']
	prepopulated_fields = {'slug':('title',)}

class PostImagesAdmin(admin.ModelAdmin):
	pass

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(PostImages, PostImagesAdmin)