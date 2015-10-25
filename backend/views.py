# django imports
# from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
# from django.views.decorators.csrf import csrf_exempt
# rest_framework imports
from rest_framework import generics, status, permissions
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# local imports
from backend.models import Event
from backend.serializer import EventBrowserSerializer, UserSerializer
from backend.permissions import IsOwnerOrReadOnly
# class MessageViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer
def test(request):
    return JsonResponse({'version': '0.1.0'})
# class EventViewSet(viewsets.ModelViewSet):
#     queryset = Event.objects.all()
#     serializer_class = EventBrowserSerializer




class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventBrowserSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventBrowserSerializer
    permission_classes = (permissions.IsAdminUser,)
    def get(self, request, *args, **kwargs):
        event = snippet.get_object();


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
def logout_user(request):
    return JsonResponse({'dumy':'test'})
