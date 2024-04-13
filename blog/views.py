from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse
from .models import Post, Comment
from .forms import PostForm
from django.db.models import Q


# Create your views here.

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

    return render(request, "blog/index.html", {"post_list": queryset, "not_found": not_found, "search_term": q })

@login_required
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
    comments = post.comments.all()

    if request.method == "POST":
        print(request.POST.get('body'))
        comment = Comment.objects.create(
            post=post,
            author=request.user,
            content=request.POST.get('body'),
        )
        return redirect('post_detail', slug=slug)

    return render(request, "blog/post_detail.html", {"post": post, 'comments': comments},)


@login_required(login_url='login_register')
def create_post(request):
    form = PostForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, "blog/post_form.html", {"form": form})



@login_required(login_url='login_register')
def update_post(request, id):
    post = Post.objects.get(id=id)
    form = PostForm(instance=post)
    # instance=post in order to pre-populate the form with the posts' existing values
    context = {
        "post": post,
        "form": form,
    }
    if request.user != post.author:
        return HttpResponse('You cannot update a post you did not create!')

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, "blog/post_form.html", context)


@login_required(login_url='login_register')
def delete_post(request, id):
    print(request)
    post = Post.objects.get(id=id)

    if request.user != post.author:
        return HttpResponse("You cannot delete this resource")

    
    if request.method == "POST":
        print("Deleting post: " + id)
        Post.objects.get(id=id).delete()
        return redirect('home')
    return render(request, "blog/post_delete.html", {"post": post})

def login_view(request):
    page = 'login'
    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.error(request, 'Successully logged in!')
                
        except:
            messages.error(request, 'Username or password incorrect')

    
    return render(request, 'login_register.html', {'page': page})

def user_logout(request):
    logout(request)
    return redirect('home')

def user_register(request):
    page = 'register'

    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # The commit=False argument passed to the save() method 
            # indicates that the changes made to the user instance 
            # should not be immediately saved to the database. 
            # This allows additional modifications to be made 
            # to the user instance before it's saved permanently.
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else: 
            messages.error(request,'An error occurred during registraion, please try again')
        
    return render(request, "login_register.html", {'page': page, "form": form})