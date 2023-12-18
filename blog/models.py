from django.db import models
# Create your models here.
class Post (models.Model):
    #author
    #image
    title = models.CharField(max_length = 255)
    content = models.TextField()
    #category
    #tag
    status = models.BooleanField(default=False)
    counted_view = models.IntegerField(default=0)
    published_date = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)