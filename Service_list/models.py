from __future__ import unicode_literals

from django.db import models
from Home.models import Category

# Create your models here.

class ServiceList(models.Model):
	service_id = models.AutoField(primary_key=True)
	category_id = models.ForeignKey(Category, null=True,blank=True)
	service_name = models.CharField(max_length = 25)
