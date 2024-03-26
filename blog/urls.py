from . import views
from django.urls import path

urlpatterns = [
    path('blog/posts/', views.PostList.as_view(), name='post_list'),
]