'''EVENT VIEWS'''
# django imports
from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework import generics, status, permissions
#local imports
from backend.models import Event
from backend.serializer import EventBrowserSerializer
from backend.permissions import IsOwnerOrReadOnly


'''LISTS ALL EVENTS'''
class List(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventBrowserSerializer
    #permission_classes = (permissions.IsAuthenticated,)
    #def perform_create(self, serializer):
        #serializer.save(owner=self.request.user)


'''GIVES DETAILS OF AN EVENT'''
class Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventBrowserSerializer
    permission_classes = (permissions.IsAdminUser,)
    def get(self, request, *args, **kwargs):
        event = snippet.get_object();

