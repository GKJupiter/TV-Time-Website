from django.db import models
from django.contrib.auth.models import User

class Media(models.Model):
    title = models.CharField(max_length=200)
    tvmaze_id = models.IntegerField(unique=True)
    poster_url = models.URLField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)

class UserMediaTrack(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    score = models.IntegerField(default=0)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    nickname = models.CharField(max_length=50, unique=True, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    followers = models.ManyToManyField(User, related_name='following', blank=True)
    
    def __str__(self):
        return f"{self.nickname or self.user.username}'s Profile"
