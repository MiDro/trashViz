from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from processing import views

# API endpoints
urlpatterns = [
    url(r'^root/$', views.APIRoot.as_view(), name='api_root'),
    url(r'^objects/26247/$', views.api_put, name='api_put'),
    url(r'^slms/multisensor/v1.0/objects/26247/$', views.api_put, name='api_put'),
    url(r'^slms/multisensor/v1.0/objects/26247/$', views.api_put, name='api_put'),
    url(r'^slms/multisensor/v1.0/objects/26247$', views.api_put, name='api_put'),
    url(r'^slms/multisensor/v1.0/objects/26241$', views.api_put, name='api_put'),
    url(r'^trashcans/$', views.TrashList.as_view(), name='trashcan-list'),
    url(r'^trashcans/(?P<pk>[0-9]+)$', views.TrashDetail.as_view(), name='trashcan-detail'),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)$', views.UserDetail.as_view(), name='user-detail'),
    url(r'^.*/$', views.api_put, name='api_put'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)

# login and logout views for browsable APIs
urlpatterns += [url(r'^api-auth/',
                    include('rest_framework.urls',
                            namespace='rest_framework')),
                ]
