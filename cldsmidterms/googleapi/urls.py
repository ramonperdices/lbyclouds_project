from django.conf.urls import url
from . import views

app_name = 'googleapi'

urlpatterns = [
    url(r'^$', views.Home),
    url(r'^profile/$', views.update_profile),
    url(r'^account/logout/$', views.Logout),
    url(r'^maps/$', views.Maps, name='maps'),
]