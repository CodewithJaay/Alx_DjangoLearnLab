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

    # Comment CRUD URLs (nested under posts)
    path('post/<int:post_id>/comments/new/', views.CommentCreateView.as_view(), name='comment_create'),
    path('post/<int:post_id>/comments/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment_update'),
    path('post/<int:post_id>/comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),

    # Authentication URLs
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]
