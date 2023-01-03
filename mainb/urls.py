from django.urls import path, include
from . import views
from .views import SignUpView

urlpatterns = [
    path('', views.index, name='blog'),
    path('posts/', views.BlogPostListView.as_view(), name='all-posts'),
    path('post/<int:pk>', views.BlogPostDetailView.as_view(), name='view-post'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('authors/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('topics/', views.TopicListView.as_view(), name='topics'),
    path('topics/<int:pk>', views.TopicDetailView.as_view(), name='topic-detail'),
    path('myposts/', views.PostedByAuthorListView.as_view(), name='my-posted'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
