# core_user/urls.py
from django.conf.urls import url

from .import views

urlpatterns = [
    url(r'^users$', views.list_users, name='list_users'),
    # url(r'^create_user/$', views.create_user, name='create_user'),
    url(r'^(?P<core_user_id>[0-9]+)/edit_user/$', views.edit_user, name='edit_user'),
    url(r'^(?P<core_user_id>[0-9]+)/add_email_sms/$', views.add_email_sms, name='add_email_sms'),
    url(r'^profile/(?P<core_user_id>[0-9]+)/$', views.user_detail, name='user_detail'),
]
