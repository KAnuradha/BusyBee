from .models import *
from rest_framework import *


class ServiceListSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ServiceList
		fields = ('category_id_id','service_id', 'service_name')