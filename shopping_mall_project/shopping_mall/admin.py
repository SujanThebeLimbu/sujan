from django.contrib import admin
from .models import Store, Product, Sale, SaleItem, Customer, Profile


admin.site.register(Store)
admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(SaleItem)
admin.site.register(Customer)
admin.site.register(Profile)
