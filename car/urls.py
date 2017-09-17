# car/urls.py
from django.conf.urls import url

from .import views

urlpatterns = [

    url(r'^dashboard/$', views.not_authorized, name='not_authorized'),
    url(r'^(?P<car_id>[0-9]+)/$', views.car_detail, name='car_detail'),
    url(r'^car_maker/(?P<maker_id>[0-9]+)/$', views.car_maker_detail, name='maker_detail'),
    url(r'^car_list/$', views.car_list, name='car_list'),
    url(r'^car_maker_list/$', views.car_maker_list, name='maker_list'),
]
