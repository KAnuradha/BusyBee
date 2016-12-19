from rest_framework import *
from Home.models import *


class CategorySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Category
		fields = ('category_id' ,'category_name')


class CategoryAddressSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = CategoryAddress
		fields = ('category_id' ,'address', 'phone_no')



