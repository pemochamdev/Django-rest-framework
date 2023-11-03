from django.shortcuts import render, get_object_or_404

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response

from shop.models import Category, Product
from shop.serialisers import CategorySerializer, ProductSerializer

class CategoryViewset(ReadOnlyModelViewSet):
 
    serializer_class = CategorySerializer
 
    def get_queryset(self):
        return Category.objects.all()

class ProductAPIView(APIView):
    def get(self, *args, **kwargs):
        products = Product.objects.all()
        serialiser = ProductSerializer(products, many=True)

        return Response(serialiser.data)