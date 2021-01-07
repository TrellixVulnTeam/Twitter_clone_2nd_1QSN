import django
from django.utils import timezone

from django.contrib.auth.models import AbstractUser, User
from django.db import models

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.CharField(max_length=248)
    created_data = models.DateTimeField(default=django.utils.timezone.now)
    like = models.IntegerField(default=0,null=True)

    def create(self):
        self.created_data = django.utils.timezone.now()
        self.save()

    def __str__(self):
        return self.post



