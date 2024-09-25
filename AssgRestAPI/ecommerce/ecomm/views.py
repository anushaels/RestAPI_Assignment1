from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from .models import Customer,Order,OrderItem
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from .serializers import CustomerSerializer, OrderSerializer, OrderItemSerializer


# Create your views here.





@csrf_exempt
def customer_list(request):
    if request.method =="GET":
        customer_list=Customer.objects.all()
        customer_list_serializer=CustomerSerializer(customer_list,many=True)
        return JsonResponse(customer_list_serializer.data,safe=False,status=200)
    elif request.method =="POST":
        request_data=JSONParser().parse(request)
        customer_add_serializer=CustomerSerializer(data=request_data)
        if customer_add_serializer.is_valid():
            customer_add_serializer.save()
            return JsonResponse(customer_add_serializer.data,status=201)
        return JsonResponse(customer_add_serializer.errors,status=400)

@csrf_exempt
def customer_list_view(request,passed_id):
    customer_details=Customer.objects.get(c_id=passed_id)
    if request.method =="GET" or request.method=="HEAD":
        customer_details_serializer=CustomerSerializer(customer_details)
        return JsonResponse(customer_details_serializer.data,safe=False,status=200)
    elif request.method=="PUT":
        request_data = JSONParser().parse(request)
        customer_update_serializer = CustomerSerializer(customer_details, data=request_data)
        if customer_update_serializer.is_valid():
            customer_update_serializer.save()
            return JsonResponse(customer_update_serializer.data, safe=False, status=201)
        return JsonResponse(customer_update_serializer.errors, status=400)
    elif request.method == "DELETE":
        customer_details.delete()
        return HttpResponse(status=204)

@csrf_exempt
def order_list(request):
    if request.method =="GET":
        order_lists=Order.objects.all()
        order_list_serializer=OrderSerializer(order_lists,many=True)
        return JsonResponse(order_list_serializer.data,safe=False,status=200)
    elif request.method =="POST":
        request_data=JSONParser().parse(request)
        order_add_serializer=OrderSerializer(data=request_data)
        if order_add_serializer.is_valid():
            order_add_serializer.save()
            return JsonResponse(order_add_serializer.data,status=201)
        return JsonResponse(order_add_serializer.errors,status=400)

@csrf_exempt
def order_list_view(request,passed_id):
    order_details=Order.objects.get(id=passed_id)
    if request.method =="GET" or request.method=="HEAD":
        order_details_serializer=OrderSerializer(order_details)
        return JsonResponse(order_details_serializer.data,safe=False,status=200)
    elif request.method=="PUT":
        request_data = JSONParser().parse(request)
        order_update_serializer = OrderSerializer(order_details, data=request_data)
        if order_update_serializer.is_valid():
            order_update_serializer.save()
            return JsonResponse(order_update_serializer.data, safe=False, status=201)
        return JsonResponse(order_update_serializer.errors, status=400)
    elif request.method == "DELETE":
        order_details.delete()
        return HttpResponse(status=204)

@csrf_exempt
def orderitem_list(request):
    if request.method =="GET":
        orderitem_lists=OrderItem.objects.all()
        orderitem_list_serializer=OrderItemSerializer(orderitem_lists,many=True)
        return JsonResponse(orderitem_list_serializer.data,safe=False,status=200)
    elif request.method =="POST":
        request_data=JSONParser().parse(request)
        orderitem_add_serializer=OrderItemSerializer(data=request_data)
        if orderitem_add_serializer.is_valid():
            orderitem_add_serializer.save()
            return JsonResponse(orderitem_add_serializer.data,status=201)
        return JsonResponse(orderitem_add_serializer.errors,status=400)
@csrf_exempt
def orderitem_list_view(request,passed_id):
    orderitem_details=Order.objects.get(id=passed_id)
    if request.method =="GET" or request.method=="HEAD":
        orderitem_details_serializer=OrderItemSerializer(orderitem_details)
        return JsonResponse(orderitem_details_serializer.data,safe=False,status=200)
    elif request.method=="PUT":
        request_data = JSONParser().parse(request)
        orderitem_update_serializer = OrderItemSerializer(orderitem_details, data=request_data)
        if orderitem_update_serializer.is_valid():
            orderitem_update_serializer.save()
            return JsonResponse(orderitem_update_serializer.data, safe=False, status=201)
        return JsonResponse(orderitem_update_serializer.errors, status=400)
    elif request.method == "DELETE":
        orderitem_details.delete()
        return HttpResponse(status=204)