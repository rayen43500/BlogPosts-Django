from django.urls import path

from . import views

app_name = 'Posts'

urlpatterns = [
    path('', views.BlogView.as_view(), name='listhtml'),
    path('posts/new/', views.BlogCreateView.as_view(), name='create'),
    path('posts/<int:pk>/edit/', views.BlogUpdateView.as_view(), name='update'),
    path('posts/<int:pk>/delete/', views.BlogDeleteView.as_view(), name='delete'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('authors/new/', views.AuthorCreateView.as_view(), name='author-create'),
]
