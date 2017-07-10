from django.conf.urls import url 
from rest_framework.urlpatterns import format_suffix_patterns
from processing import views

urlpatterns = [
    url(r'^trashcans/$', views.trash_list),
    url(r'^trashcans/(?P<pk>[0-9]+)$', views.trash_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
