from django.conf.urls import patterns, include, url
# from rest_framework import routers
from . import views

# router = routers.DefaultRouter(trailing_slash=False)
# router.register(r'events', views.EventViewSet)

urlpatterns = [
    url(r'^$', views.test),
    url(r'^logout/', views.logout_user),
    url(r'^events/', views.EventList.as_view()),
    url(r'^events/(?P<pk>[0-9]+)/$', views.EventDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
