from django.db import models
from django.utils import timezone


# Create your models here.
class Post (models.Model):
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=200)


    def __str__(self):
        return self.text



class Comment (models.Model):
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
