from django.conf.urls import url
from django.contrib import admin


from . import views

urlpatterns = [

    url(r'^$', views.thing_list,name='list'),      #raw string  empty string(no extra path) , name of u rl
    url(r'(?P<thing_pk>\d+)/i(?P<step_pk>\d+)/$', views.step_detail1, name='step1'),
    url(r'(?P<thing_pk>\d+)/(?P<step_pk>\d+)/$', views.step_detail, name='step'),

    url(r'(?P<pk>\d+)/$',views.thing_detail,name='detail'),



]
