from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    # path("home/", views.home, name="home"),
    path("manage_stores/", views.manage_stores, name="manage_stores"),
    path(
        "manage_inventory/", views.manage_inventory, name="manage_inventory"
    ),  # URL for managing inventory
    path(
        "process_sales/", views.process_sales, name="process_sales"
    ),  # URL for processing sales
    path(
        "manage_customers/", views.manage_customers, name="manage_customers"
    ),  # URL for managing customers
    path("login/", views.user_login, name="user_login"),  # URL for user login
    path("logout/", views.logout_view, name="logout"),
    path("add_item/", views.add_item, name="add_item"),
    path("delete_item/", views.delete_item, name="delete_item"),
]
