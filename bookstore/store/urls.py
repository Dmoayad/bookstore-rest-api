from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')
router.register('authors', AuthorViewSet, basename='author')
router.register('genres', GenreViewSet, basename='genre')
router.register('books', BookViewSet, basename='book')
router.register('customers', CustomerViewSet, basename='customer')
# Register OrderViewSet but note that DefaultRouter still creates detail path by default
router.register('orders', OrderViewSet, basename='order')
router.register('orderitems', OrderItemViewSet, basename='orderitem') # Registered OrderItemViewSet
router.register('reviews', ReviewViewSet, basename='review')       # Registered ReviewViewSet

urlpatterns = [
  path('api/', include(router.urls)),
  path('api/<int:pk>/', include(router.urls)),


]
