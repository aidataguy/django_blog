from django.db import models
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE,)
    body = models.TextField()
    hero_image = models.ImageField(null=True, upload_to="img/hero_image/")
    thumb_image = models.ImageField(null=True, upload_to="img/thumb_image/")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
