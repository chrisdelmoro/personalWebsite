from django.urls import path
from . import views

urlpatterns = [
	path('home/', views.blog, name='blog'),
	path('<slug:slug>/', views.detail, name='post_detail')
]