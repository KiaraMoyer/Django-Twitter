from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):
    user = models.ForeignKey(User, related_name='tweets', on_delete=models.DO_NOTHING)
    body = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)
