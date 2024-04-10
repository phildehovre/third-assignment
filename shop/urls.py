from django.urls import path
from . import views

urlpatterns = [
    path("", views.item_list, name="shop"),
    path("login/", views.login_view, name="login_register"),
    path("item_list/<str:item_id>/", views.item_detail, name="item_detail"),
]