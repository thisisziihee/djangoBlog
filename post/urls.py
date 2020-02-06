from django.urls import path
from post import views

urlpatterns = [
    path('post_write/', views.post_write, name = 'post_write'),
    path('post_list/', views.post_list, name = 'posts_list'),
    path('post_detail/<int:post_id>', views.post_detail, name = "post_detail"),
    path('post_like/', views.post_like, name = "post_like"),
]