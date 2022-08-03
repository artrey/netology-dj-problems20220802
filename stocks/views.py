from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from stocks.models import Product, Stock
from stocks.permissions import IsOwner
from stocks.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
