from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer

from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter,OrderingFilter, DjangoFilterBackend] 
    filterset_fields = ['title',]
    search_fields = ['title',]


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [SearchFilter, OrderingFilter,DjangoFilterBackend]
    filterset_fields = ['address', 'positions','products']
    search_fields = ['address','positions','products']
