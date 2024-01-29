from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from orders.models import OrderedItems, Orders
from orders.serializer import OrderItemSerializer, OrderSerializer

@api_view(['GET'])
def orders(request):
    
    if request.method == 'GET':
      ord_obj=Orders.objects.all()
      serializer = OrderSerializer(ord_obj, many=True)
      return Response(serializer.data) 

# Create your views here.
