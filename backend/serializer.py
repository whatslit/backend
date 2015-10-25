'''serializer.py'''
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Comment, Event

class UserSerializer(serializers.ModelSerializer):
    events = serializers.PrimaryKeyRelatedField(many=True, queryset=Event.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'events')
class EventBrowserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('name', 'event_type', 'time_posted', 'latitude', 'longitude', 'score')
