from django.conf.urls import patterns, include, url
from . import views



urlpatterns = [
    url(r'^$', views.main.version),
    url(r'^events/', views.event.List.as_view()),
    url(r'^events/(?P<pk>[0-9]+)/$', views.event.Detail.as_view()),
    url(r'^users/$', views.user.List.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.user.Detail.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
