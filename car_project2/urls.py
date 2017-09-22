# Project URL
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from car.views import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^user_profile/', include('core_user.urls', namespace="user_profile")),
    url(r'^vehicle/', include('car.urls', namespace='vehicle')),

    url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'registration/logged_out.html'}, name='logout'),
    url(r'^admin/', admin.site.urls),
]
