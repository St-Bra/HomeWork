from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import viewsets
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Product, Warehouse, Stock, Supply, SuppliedProduct
from .serializers import (
    ProductSerializer,
    WarehouseSerializer,
    StockSerializer,
    SupplySerializer,
    SuppliedProductSerializer,
)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    @method_decorator(cache_page(60 * 5))  # 5 минут
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        instance = serializer.save()
        cache.clear()
        return instance

    def perform_update(self, serializer):
        instance = serializer.save()
        cache.clear()
        return instance

    def perform_destroy(self, instance):
        instance.delete()
        cache.clear()

class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    permission_classes = [IsAuthenticated]

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [IsAuthenticated]

class SupplyViewSet(viewsets.ModelViewSet):
    queryset = Supply.objects.all()
    serializer_class = SupplySerializer
    permission_classes = [IsAuthenticated]

class SuppliedProductViewSet(viewsets.ModelViewSet):
    queryset = SuppliedProduct.objects.all()
    serializer_class = SuppliedProductSerializer
    permission_classes = [IsAuthenticated]


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response({'message': f'Hello, {request.user.username}!'})