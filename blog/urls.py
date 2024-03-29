from django.urls import path

from . import views

urlpatterns = [
	path('', views.blog, name='blog'),
	path('search/', views.search, name='search'),
	path('tag/<slug:slug>/', views.tag, name='tag_detail'),
	path('category/<slug:slug>/', views.category, name='category_detail'),
	path('<slug:category_slug>/<slug:slug>/', views.detail, name='post_detail'),

]