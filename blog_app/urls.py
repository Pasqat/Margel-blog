from django.urls import path
from . import views

app_name = 'blog_app'
urlpatterns = [
    path('', views.latest, name='index'),
    path('latest/', views.latest, name='latest'),
    path('new/', views.new_article, name='new'),
    path('<int:article_id>/', views.read_article, name='read'),
]