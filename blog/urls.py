from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.gonderi_list, name='gonderi_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.gonderi_detay, name='gonderi_detay'),
    url(r'^post/new/$', views.yeni_gonderi, name='yeni_gonderi'),
     url(r'^post/(?P<pk>[0-9]+)/edit/$', views.gonderi_duzenle, name='gonderi_duzenle'),
]