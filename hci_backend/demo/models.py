from django.db import models

# Create your models here.

class Video(models.Model):
    video_id = models.BigAutoField(primary_key=True)
    video_path = models.CharField(max_length=200)
    video_score = models.IntegerField()
    related_audio = models.CharField(max_length=60)


class Audio(models.Model):
    audio_id = models.BigAutoField(primary_key=True)
    audio_path = models.CharField(max_length=200)
    audio_scroe = models.IntegerField()
    related_video = models.CharField(max_length=60)
    transcript = models.TextField()

       
