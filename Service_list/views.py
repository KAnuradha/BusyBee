from django.shortcuts import render
from rest_framework import status,permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.db.models import Q
from django.db.models.query import QuerySet
from Home.models import *

# Create your views here.


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def  service_list(request,id):
	if request.method == 'GET':
		category = Category.objects.get(category_id = id)
		service = ServiceList.objects.filter(Q(category_id=category))
		serializer = ServiceListSerializer(service, many = True)
		return Response(serializer.data)