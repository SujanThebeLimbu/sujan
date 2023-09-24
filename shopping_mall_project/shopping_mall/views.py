from django.shortcuts import render, redirect
from .models import Store, Product, Sale, SaleItem, Customer
from .forms import StoreForm, ProductForm, SaleForm, SaleItemForm, CustomerForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import get_object_or_404


def homepage(request):
    return render(request, "homepage.html")


def custom_login(request):
    # Handle the login form submission
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Determine the user's role and redirect accordingly
            profile = (
                user.profile
            )  # Assuming you have a one-to-one relationship with Profile
            if profile.role == "Admin":
                return redirect(request, "home_admin.html")
            elif profile.role == "STORE_MANAGER":
                return redirect("store_manager_home")
            elif profile.role == "CASHIER":
                return redirect("cashier_home")
            elif profile.role == "CUSTOMER":
                return redirect("customer_home")
    return render(request, "login.html")  # Display the login form


def logout_view(request):
    logout(request)
    return redirect("homepage")


def manage_stores(request):
    stores = Store.objects.all()
    return render(request, "manage_stores.html", {"stores": stores})


def manage_inventory(request):
    # Retrieve the list of products from the database
    products = Product.objects.all()
    return render(request, "manage_inventory.html", {"products": products})


def add_item(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        product = Product.objects.get(id=product_id)
        # Implement logic to add the item to the inventory here.
        # You can update the stock_level field of the product object.
        # Example: product.stock_level += 1
        # Then, save the updated product.
        product.save()
    return redirect("manage_inventory")


def delete_item(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")

        # Use get_object_or_404 to retrieve the product or return a 404 response if it doesn't exist.
        product = get_object_or_404(Product, id=product_id)

        # Delete the product from the database.
        product.delete()

    return redirect("manage_inventory")


def process_sales(request):
    # Implement sales processing logic here
    if request.method == "POST":
        sale_form = SaleForm(request.POST)
        if sale_form.is_valid():
            # Process the sale and update inventory
            sale = sale_form.save()
            # You may need to update stock levels here
            return redirect("manage_sales")  # Redirect to the sales management page
    else:
        sale_form = SaleForm()

    return render(request, "process_sales.html", {"sale_form": sale_form})


def manage_customers(request):
    # Retrieve the list of customers from the database
    customers = Customer.objects.all()
    return render(request, "manage_customers.html", {"customers": customers})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect(
                    "homepage"
                )  # Redirect to the homepage after successful login
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})
