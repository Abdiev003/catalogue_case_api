from django.urls import path

from products.views import (
    CategoryListCreateAPIView,
    CategoryRetrieveAPIView,
    ProductCreateAPIView,
    ProductRetrieveAPIView,
    ProductListAPIView,
    ProductFavoriteAPIView
)

urlpatterns = [
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list'),
    path('categories/<int:id>/', CategoryRetrieveAPIView.as_view(), name='category-detail'),

    path('categories/<int:id>/products/', ProductListAPIView.as_view(), name='product-list'),

    path('products/', ProductCreateAPIView.as_view(), name='product-create'),
    path('products/<int:id>/', ProductRetrieveAPIView.as_view(), name='product-detail'),

    path('favorite/', ProductFavoriteAPIView.as_view(), name='product-favorite'),
]