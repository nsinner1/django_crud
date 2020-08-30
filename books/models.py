from django.db import models
from django.urls import reverse

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    body = models.TextField(default='Enter Descriptions:')
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')

    def post_absolute_url(self):
        return reverse('home')