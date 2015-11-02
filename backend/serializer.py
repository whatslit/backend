'''serializer.py'''
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Comment, Event

class UserSerializer(serializers.ModelSerializer):
    events = serializers.PrimaryKeyRelatedField(many=True, queryset=Event.objects.all())

    class Meta:
        model = User
        fields = ('id',  'username', 'email', 'password', 'events',)
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class EventBrowserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'owner', 'name', 'event_type', 'time_posted', 'latitude', 'longitude', 'score')
        #extra_kwargs = {'owner': {'read_only': True}}