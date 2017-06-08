from django.conf.urls import url
from . import views

app_name = 'map'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'(?P<trashCan_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<trashCan_id>[0-9]+)/$', views.detail, name='detail'),
]
