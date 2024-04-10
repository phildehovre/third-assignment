from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Post
from .forms import PostForm, CommentForm
from django.db.models import Q


# Create your views here.


# class PostList(generic.ListView):
#     '''
#     When an instance of PostList is rendered 
#     and the corresponding template (index.html) 
#     is rendered, the post_list context variable 
#     is automatically available in the template.
#     '''
#     queryset = Post.objects.filter(status=1)
#     template_name = "blog/index.html"
#     paginate_by = 6

def post_list(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    published = Post.objects.filter(status=1)
    queryset = published.filter(
        Q(title__icontains=q) |    # Title contains search term
        Q(author__username__icontains=q) |    # Author username contains search term
        Q(content__icontains=q) 
    )

    not_found = len(queryset) == 0

    if not_found: 
       queryset = published

    print(not_found)

    return render(request, "blog/index.html", {"post_list": queryset, "not_found": not_found })


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



def create_post(request):
    form = PostForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, "blog/post_form.html", {"form": form})


def update_post(request, id):
    post = Post.objects.get(id=id)
    form = PostForm(instance=post)
    context = {
        "post": post,
        "form": form,
    }
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, "blog/post_form.html", context)

def delete_post(request, id):
    post = Post.objects.get(id=id)
    if request.method == "POST":
        print("Deleting post: " + id)
        Post.objects.get(id=id).delete()
        return redirect('home')
    return render(request, "blog/post_delete.html", {"post": post})