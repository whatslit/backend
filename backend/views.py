from django.shortcuts import render
from django.http import HttpResponse
from .models import Event
from rest_framework import viewsets
from .serializer import EventBrowserSerializer

# Create your views here.

# class MessageViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventBrowserSerializer
def index(request):
	return HttpResponse("Test")
