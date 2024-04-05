from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

# Create your views here.


class PostList(generic.ListView):
    '''
    When an instance of PostList is rendered 
    and the corresponding template (index.html) 
    is rendered, the post_list context variable 
    is automatically available in the template.
    '''
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """
    queryset = Post.objects.filter(status=1)
    # get_object_or_404() is a shortcut function that handles the case when an object is not found.
    post = get_object_or_404(queryset, slug=slug)
    return render(request, "blog/post_detail.html", {"post": post},)