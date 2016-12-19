from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Category(models.Model):
	category_id = models.AutoField(primary_key=True)
	category_name = models.CharField(max_length = 25)


class CategoryAddress(models.Model):
	category_id = models.ForeignKey(Category, null=True,blank=True)
	address = models.CharField(max_length = 100)
	phone_no = models.CharField(max_length = 25)