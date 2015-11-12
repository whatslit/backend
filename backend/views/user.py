'''USER VIEW'''

# django imports
from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework import generics, status, permissions
from backend.serializer import UserSerializer
from backend.permissions import IsOwnerOrReadOnly


class List(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_class = (permissions.IsAdminUser,)

class Detail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
    	pass
    	
