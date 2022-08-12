from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status

from .serializers import ProductSerializer, SubscribeProductSerializer

from .models import Product

class SubscribeView(APIView):

    def get(self, request):
        active_products = Product.objects.filter(is_active=True)
        product_serializer_data = ProductSerializer(active_products, many=True).data
        return Response(product_serializer_data)
        
        
    def post(self, request):
        subscribed_serializer_data = SubscribeProductSerializer(data = request.data)
        if subscribed_serializer_data.is_valid():
            subscribed_serializer_data.save()
            return Response({"message":"구독완료"}, status=status.HTTP_200_OK)
        return Response(subscribed_serializer_data.errors, status=status.HTTP_400_BAD_REQUEST) 
        