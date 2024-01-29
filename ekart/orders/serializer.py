from rest_framework import serializers
from orders.models import Orders, OrderedItems


class OrderSerializer(serializers.ModelSerializer) :
    
     class Meta:
        model = Orders
        fields = '__all__'
        


class OrderItemSerializer(serializers.ModelSerializer) :
    
     class Meta:
        model = OrderedItems
        fields = '__all__'