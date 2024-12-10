from django.db import models

# Create your models here.


class Comment(models.Model):
    author = models.CharField(max_length=20)
    content = models.TextField(blank=True, null=True)
    like = models.BooleanField(default=False)
