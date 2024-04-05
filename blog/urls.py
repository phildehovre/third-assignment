from . import views
from django.urls import path

urlpatterns = [
    # PostList.as_view() is a class-based view that will display a list of all the posts.
    path('blog/posts/', views.PostList.as_view(), name='post_list'),

    # post_detail is a function-based view that will display an individual post.
    # <slug:slug>/ is a URL pattern that will match a slug string and pass it to the view as a keyword argument.
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]