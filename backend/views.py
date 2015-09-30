from django.shortcuts import render
from django.http import HttpResponse
from .models import Message
from rest_framework import viewsets
from .serializer import MessageSerializer

# Create your views here.

class MessageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

def index(request):
	return HttpResponse("What's Lit?")
