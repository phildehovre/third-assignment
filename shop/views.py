from django.shortcuts import render
from .models import Product



# Create your views here.



def item_list(request):
    items = Product.objects.all()
    return render(request, 'shop/item_list.html', context={'items': items})


def item_detail(request, item_id):
    product = Product.objects.get(id=item_id)

    return render(request, 'shop/item_detail.html', context={'item': product})


