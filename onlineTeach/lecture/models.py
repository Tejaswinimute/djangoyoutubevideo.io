from django.db import models
from embed_video.fields import EmbedVideoField

class Containt(models.Model):
    id = models.AutoField
    video = EmbedVideoField()
    title = models.CharField(max_length=30)
    desc = models.CharField(max_length=500)
    date = models.DateField()


    def __str__(self):
        return self.title
