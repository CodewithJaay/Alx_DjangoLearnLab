from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    
    # Post CRUD URLs
    path('post/', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),

    # Comment CRUD URLs 
    path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),

    # Authentication URLs
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),

    # Search & Tag URLs
    path('search/', views.search_posts, name='search_posts'),
    path('tags/<slug:tag_slug>/', views.PostByTagListView.as_view(), name='posts_by_tag'),
]

