from django.urls import path
from blog_app import views

app_name = 'blog_app'

urlpatterns =[
    path('', views.ArticleListView.as_view(), name='article_list'),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name='article_detail'),
    path('article/new/', views.CreateArticleView.as_view(), name='article_new'),
    path('article/<int:pk>/edit/', views.ArticleUpdateView.as_view(), name='article_edit'),
    path('article/<int:pk>/remove/', views.ArticleDeleteView.as_view(), name='article_remove'),
    path('drafts/', views.DraftListView.as_view(), name='article_draft_list'),
    path('article/<int:pk>/publish', views.article_publish, name='article_publish'),
    path('category/<category>/', views.CategoryListView.as_view(), name='category_list'),
    path('tag/<tag>/', views.TagListView.as_view(), name='tag_list'),
    path('search/<search>/', views.ArticleSearchView.as_view(), name='search_article'),
    path('article/<int:pk>/comment/', views.add_comment_to_article, name='add_comment_to_article'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove')
]