from . import views
from django.urls import path

urlpatterns = [
    # PostList.as_view() is a class-based view that will display a list of all the posts.

    # post_detail is a function-based view that will display an individual post.
    # <slug:slug>/ is a URL pattern that will match a slug string and pass it to the view as a keyword argument.
    # to the left of the ':' is the converter type, and to the right is the name of the keyword argument that will be passed to the view.
    path('', views.post_list, name='home'),
    path('create-post/', views.create_post, name='create_post'),
    path('update-post/<str:id>', views.update_post, name='update_post'),
    path('delete-post/<str:id>', views.delete_post, name='delete_post'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]