from django.shortcuts import render
from .models import Product


# Create your views here.



def item_list(request):
    items = Product.objects.all()
    return render(request, 'shop/item_list.html', context={'items': items})


def item_detail(request, item_id):
    product = Product.objects.get(id=item_id)

    return render(request, 'shop/item_detail.html', context={'item': product})

def login_view(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        context = {'username':username, 'password': password}

    return render(request, 'login_register.html', context)