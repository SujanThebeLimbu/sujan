from django import forms
from .models import Store, Product, Sale, SaleItem, Customer

# from django.contrib.auth.forms import UserCreationForm

# from .models import CustomUser


# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = ["username", "password1", "password2", "role"]


class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = "__all__"


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = "__all__"


class SaleItemForm(forms.ModelForm):
    class Meta:
        model = SaleItem
        fields = "__all__"


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
