from django.db import models
from apps.common.models import BaseModel
from apps.movies.models import *
# Create your models here.


class WatchSession(BaseModel):
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    device = models.CharField(max_length=200)
    language = models.ForeignKey(Language,on_delete=models.PROTECT)
    country = models.ForeignKey(Country,on_delete=models.CASCADE,null=True,blank=True)
    subtitle = models.ForeignKey(MovieSubtitle,on_delete=models.CASCADE)
    quality = models.CharField(max_length=10,choices=QUALITY_CHOICES,default="720p")
    
    def __str__(self):
        return f"{self.movie.title} ({self.quality})"
    

class Like(BaseModel):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    watch_session = models.ForeignKey(WatchSession, on_delete=models.SET_NULL,null=True)
    

    def __str__(self):
        return f"{self.movie.title} "
    
class Comment(BaseModel):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    watch_session = models.ForeignKey(WatchSession, on_delete=models.SET_NULL, null=True)
    
    text = models.TextField()

    def __str__(self):
        return f"{self.movie.title} "
    