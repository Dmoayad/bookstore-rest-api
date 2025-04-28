from django.contrib import admin
from .models import (
    Article,  # Keep this if you still want to manage Articles in the admin
    Author,
    Genre,
    Book,
    Customer,
    Order,
    OrderItem,
    Review,
)

# Register your models here.
admin.site.register(Article) # Keep this if needed
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Review)