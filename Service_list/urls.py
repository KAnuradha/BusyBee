from django.conf.urls import url
from . import views


urlpatterns = [
		url(r'^(?P<id>[\w\-]+)/$', views.service_list, name='service_list'),
		]