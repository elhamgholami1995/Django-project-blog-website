from django.db import models
from django.shortcuts import reverse


class Post(models.Model):
    STASUSE_CHOICES = (
        ('pub', 'public'),
        ('drf', 'draft'),
    )
    title = models.CharField(max_length=100)
    text = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STASUSE_CHOICES, max_length=3)
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.id])