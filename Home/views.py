from django.shortcuts import render
from rest_framework import status,permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import *
from .serializers import *



@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def home(request):
	if request.method == 'GET':
		category = Category.objects.all()
		address = CategoryAddress.objects.all()
		# serializer = CategorySerializer(category, many=True)
		result = list()
		for i in category:
			for j in address:
				if i.category_id == j.category_id_id:
					d = {}
					d['category_id'] = i.category_id
					d['category_name'] = i.category_name
					d['address'] = j.address
					d['phone_no'] = j.phone_no
					result.append(d)
		d2 = {}
		d2['service_list_url'] = "http://127.0.0.1:8000/service_list"
		result.append(d2)
		print result

		return Response(result)
	


	



