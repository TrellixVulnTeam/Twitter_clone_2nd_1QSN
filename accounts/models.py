import django
from django.utils import timezone

from django.contrib.auth.models import AbstractUser, User
from django.db import models

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.CharField(max_length=248)
    created_data = models.DateTimeField(default=django.utils.timezone.now)
    lat = models.DecimalField('緯度', max_digits=8, decimal_places=6)
    lng = models.DecimalField('経度', max_digits=9, decimal_places=6)

    def create(self):
        self.created_data = django.utils.timezone.now()
        self.save()

    def __str__(self):
        return self.post
#
# class Like(models.Model):
#     article = models.ForeignKey(Post,on_delete=models.CASCADE)
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     timestamp

