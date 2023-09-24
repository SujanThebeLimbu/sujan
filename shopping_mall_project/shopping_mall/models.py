from django.db import models
from django.contrib.auth.models import User, AbstractUser


# class User(AbstractUser):
#     # Define choices for the roles field
#     ADMIN = "admin"
#     STORE_MANAGER = "store_manager"
#     CASHIER = "cashier"
#     CUSTOMER = "customer"

#     ROLES_CHOICES = [
#         (ADMIN, "Admin"),
#         (STORE_MANAGER, "Store Manager"),
#         (CASHIER, "Cashier"),
#         (CUSTOMER, "Customer"),
#     ]


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    # Define choices for the roles field
    ADMIN = "admin"
    STORE_MANAGER = "store_manager"
    CASHIER = "cashier"
    CUSTOMER = "customer"

    ROLES_CHOICES = [
        (ADMIN, "Admin"),
        (STORE_MANAGER, "Store Manager"),
        (CASHIER, "Cashier"),
        (CUSTOMER, "Customer"),
    ]

    # Add the roles field
    role = models.CharField(
        max_length=20,
        choices=ROLES_CHOICES,
        default=CUSTOMER,  # Default role is "Customer"
    )

    def __str__(self):
        return str(self.user)


class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    contact_details = models.TextField()


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    stock_level = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Sale(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through="SaleItem")
    customer = models.ForeignKey("Customer", on_delete=models.SET_NULL, null=True)
    sale_date = models.DateTimeField(auto_now_add=True)


class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)


class Customer(models.Model):
    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    purchase_history = models.ManyToManyField(Product, through="Purchase")


class Purchase(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=50
    )  # Define roles, e.g., "admin," "manager," "cashier," "customer"

    def __str__(self):
        return self.user.username
