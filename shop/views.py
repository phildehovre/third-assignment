from django.shortcuts import render, redirect
from .models import Product, Review
from django.db.models import Q
from .forms import ReviewForm



# Create your views here.



def item_list(request):
    items = Product.objects.all()
    return render(request, 'shop/item_list.html', context={'items': items})

def item_detail(request, item_id):
    product = Product.objects.get(id=item_id)
    reviews = Review.objects.filter(Q(product__id=item_id))

    form = ReviewForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            review = form.save(commit=False)
            # Add author to the review
            review.author = request.user
            review.product = product
            review.save()
        
        # return redirect("f`/shop/item/${item_id}`")

    return render(request, 'shop/item_detail.html', context={'item': product, 'reviews': reviews, 'form': form})


    