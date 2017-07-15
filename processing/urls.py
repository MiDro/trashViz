from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from processing import views

# API endpoints
urlpatterns = [
    url(r'^root/$', views.api_root),
    url(r'^trashcans/$', views.TrashList.as_view(), name='trashcan-list'),
    url(r'^trashcans/(?P<pk>[0-9]+)$', views.TrashDetail.as_view(), name='trashcan-detail'),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)$', views.UserDetail.as_view(), name='user-detail'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)

# login and logout views for browsable APIs
urlpatterns += [url(r'^api-auth/',
                    include('rest_framework.urls',
                            namespace='rest_framework')),
                ]
