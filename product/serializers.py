from rest_framework import serializers

from user.models import User

from .models import Product, SubscribedProduct



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        
        
class SubscribeProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SubscribedProduct
        fields = "__all__"