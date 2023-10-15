from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles', blank=True, null=True)
    title = models.CharField(max_length=50)
    text = models.TextField()
    status = models.BooleanField()

    def __str__(self):
        return self.title
