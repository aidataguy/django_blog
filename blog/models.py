from django.db import models
from django.urls import reverse
from gdstorage.storage import  GoogleDriveStorage
# Create your models here.

gd_storage = GoogleDriveStorage()
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE,)
    body = models.TextField()
    hero_image = models.FileField(null=True, storage=gd_storage)
    thumb_image = models.FileField(null=True, storage=gd_storage)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
