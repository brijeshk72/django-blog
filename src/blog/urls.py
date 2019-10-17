from django.urls import path, include
from blog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog', views.blog, name='blog'),
    path('post/<id>/', views.post, name='blog'),
]