from django.conf.urls import url
from backend import views

urlpatterns = [
    url(r'^events/$', views.index),
    # url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
]
