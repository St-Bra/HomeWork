from django.urls import path
from . import views
from .views import DeletePostView

urlpatterns = [
    path('posts/', views.post_list_json, name='post_list_json'),
    path('posts/<int:pk>/', views.post_detail_json, name='post_detail_json'),
    path('', views.post_list_html, name='post-list-html'),
    path('post/<int:pk>/', views.post_detail_html, name='post-detail-html'),
    path('api/posts/<int:pk>/delete/', DeletePostView.as_view(), name='delete-post'),
]