from django.conf.urls import url
from . import views

app_name = 'map'
urlpatterns = [
<<<<<<< HEAD
    url(r'^$', views.index, name='index'),
    url(r'(?P<trashCan_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<trashCan_id>[0-9]+)/$', views.detail, name='detail'),
=======
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', 
    	views.DetailView.as_view(), 
    	name='detail'),
>>>>>>> 7512e97dbbebffe9bd6930fc0f5d29550fe116ec
]
