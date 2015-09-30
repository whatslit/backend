from django.db import models

# Create your models here.
class Message(models.Model):
    author = models.CharField(max_length=20)
    text = models.CharField(max_length=140)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.author
