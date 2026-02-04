from django.contrib import admin
from apps.store.models import BlogCategory, Blogs, Product, ProductCategory, Order, OrderItem
# Register your models here.

admin.site.register(BlogCategory)
admin.site.register(Blogs)
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Order)
admin.site.register(OrderItem)