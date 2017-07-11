from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from processing import views

urlpatterns = [
        url(r'^trashcans/$', views.TrashList.as_view()),
        url(r'^trashcans/(?P<pk>[0-9]+)$', views.TrashDetail.as_view()),
        url(r'^users/$', views.UserList.as_view()),
        url(r'^users/(?P<pk>[0-9]+)$', views.UserDetail.as_view()),
       ]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
        ]
