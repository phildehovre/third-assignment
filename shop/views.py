from django.shortcuts import render

# Create your views here.

items = [
        {
            'name': 'item1',
            'price': 100,
            'description': 'This is item1',
            'id': "1"
        },
        {
            'name': 'item2',
            'price': 200,
            'description': 'This is item2',
            'id': "2"
        },
        {
            'name': 'item3',
            'price': 300,
            'description': 'This is item3',
            'id': "3"
        },
        {
            'name': 'item4',
            'price': 400,
            'description': 'This is item4',
            'id': "4"
        },
        {
            'name': 'item5',
            'price': 500,
            'description': 'This is item5',
            'id': "5"
        },
        {
            'name': 'item6',
            'price': 600,
            'description': 'This is item6',
            'id': "6"
        },
        {
            'name': 'item7',
            'price': 700,
            'description': 'This is item7',
            'id': "7"
        },
        {
            'name': 'item8',
            'price': 800,
            'description': 'This is item8',
            'id': "8"
        },
        {
            'name': 'item9',
            'price': 900,
            'description': 'This is item9',
            'id': "9"
        },
        {
            'name': 'item10',
            'price': 1000,
            'description': 'This is item10',
            'id': "10"
        },
    ]


def item_list(request):
    return render(request, 'shop/item_list.html', context={'items': items})


def item_detail(request, item_id):
    found_item = None
    for item in items:
        if item['id'] == item_id:
            found_item = item

    return render(request, 'shop/item_detail.html', context={'item': found_item})