'''serializer.py'''
from rest_framework import serializers
from .models import Comment, Event

# class MessageSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Message
#         fields = ('author','text','timestamp',)
class EventBrowserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('name', 'event_type', 'time_posted', 'latitude', 'longitude', 'score')
