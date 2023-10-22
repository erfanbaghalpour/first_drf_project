from django.db import models
from django.contrib.auth.models import User


class BlockUser(models.Model):
    username = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.username


class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles', blank=True, null=True)
    title = models.CharField(max_length=50)
    text = models.TextField()
    image = models.ImageField(upload_to='images', blank=True, null=True)
    status = models.BooleanField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.text[:30]
