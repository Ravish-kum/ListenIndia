from django.db import models

# Create your models here.

class ListenIN(models.Model):
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='videos/')
    language = models.CharField(max_length=5)
    class Meta:
        db_table='video'