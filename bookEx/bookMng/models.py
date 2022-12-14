from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class MainMenu(models.Model):
    item = models.CharField(max_length=200, unique=True)
    link = models.CharField(max_length=500, unique=True)

    def __str__(self):
        return self.item


class Book(models.Model):
    name = models.CharField(max_length=200)
    web = models.URLField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    publishdate = models.DateField(auto_now=True)
    # favourite
    favourite = models.BooleanField(default=False)
    picture = models.FileField(upload_to='bookEx/static/uploads')
    pic_path = models.CharField(max_length=300, editable=False, blank=True)
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    # rating
    rate = models.IntegerField(default=0)


class Comment(models.Model):
    comment = models.CharField(max_length=2000)
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    book = models.CharField(max_length=200)
    book_id = models.IntegerField(default=-1)


def __str__(self):
    return str(self.id)
