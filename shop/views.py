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

    # ------------- Below: ---------------
    # Either can be used, but it is more robust to take advantage of the
    # automatic reverse relationship inferred by Django:
    """
    reviews = Review.objects.filter(Q(product__id=item_id))
    OR
    reviews = product.review_set.all()
    Note: the name "review_set" can  be overridden in the Review model
    by specifying a "related_name=<name>" property after the delete behaviour.
    """
    reviews = product.review_set.all().order_by('-created_at')

    # reviews = Review.objects.filter(Q(product__id=item_id)).order_by('-created_at')
    form = ReviewForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            review = form.save(commit=False)
            # Add author to the review
            review.author = request.user
            review.product = product
            review.save()
            product.save()
        

    return render(request, 'shop/item_detail.html', context={'item': product, 'reviews': reviews, 'form': form})


    