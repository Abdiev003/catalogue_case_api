from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    ListCreateAPIView,
    ListAPIView,
)
from rest_framework.response import Response

from products.serializers import (
    ProductSerializer,
    ProductCreateSerializer,
    CategorySerializer,
    CategoryDetailSerializer,
)
from products.models import Product, Category


class CategoryListCreateAPIView(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(status=True)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CategoryDetailSerializer
        return CategorySerializer


class CategoryRetrieveAPIView(RetrieveAPIView):
    serializer_class = CategoryDetailSerializer
    queryset = Category.objects.filter(status=True)
    lookup_field = 'id'


class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        product = Product.objects.filter(category__id=self.kwargs['id'])
        if product:
            return product

        raise ValidationError({'detail': 'Product not found'})


class ProductCreateAPIView(CreateAPIView):
    serializer_class = ProductCreateSerializer
    queryset = Product.objects.filter(status=True)


class ProductRetrieveAPIView(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(status=True)
    lookup_field = 'id'


class ProductFavoriteAPIView(CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(status=True)

    def post(self, request, *args, **kwargs):
        product_id = request.data.get('productId')
        product = Product.objects.filter(id=product_id).first()
        if product:
            product.is_favorite = True
            product.save()
            return Response(ProductSerializer(product).data, status=status.HTTP_201_CREATED)
        return Response({'detail': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)