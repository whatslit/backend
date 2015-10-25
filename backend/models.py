from django.db import models
from django.contrib.auth.models import User

PARTY = 'PA'
CONCERT = 'CO'
EVENT_TYPES = (
    (PARTY, 'Party'),
    (CONCERT, 'Concert'),
)
# Create your models here.
# class Message(models.Model):
#     author = models.CharField(max_length=20)
#     text = models.CharField(max_length=140)
#     timestamp = models.DateTimeField(auto_now_add=True)
#
#     def __unicode__(self):
#         return self.author

class Comment(models.Model):
    creator_id = models.IntegerField()
    time_posted = models.DateTimeField()
    was_removed = models.BooleanField(default=False)
    content = models.CharField(max_length=1000)
class Event(models.Model):
    owner = models.ForeignKey('auth.User', related_name='events', null=True)
    name = models.CharField(max_length=100)
    event_type = models.CharField(max_length=2, choices=EVENT_TYPES, default=PARTY)
    was_removed = models.BooleanField(default=False)
    time_posted= models.DateTimeField()
    # alternatively we can look into Textfield, however max_length restrictions are not handled for hte database
    description = models.CharField(max_length=1000)
    comments = models.ForeignKey(Comment, null=True)
    latitude = models.DecimalField(decimal_places=10, max_digits=13)
    longitude = models.DecimalField(decimal_places=10, max_digits=13)
    score = models.DecimalField(decimal_places=3, max_digits=8)
class Partier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.FileField()
    events_invited = models.ManyToManyField(Event, related_name='events')
    litness = models.DecimalField(decimal_places=5, max_digits=13, null=True)


from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
