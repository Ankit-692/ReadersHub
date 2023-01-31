from django.db import models

class Book(models.Model):
    username = models.CharField(max_length=100)
    titleName = models.CharField(max_length=100,null=True, blank=True)
    description = models.TextField(max_length=2000,null=True, blank=True)
    authors = models.CharField(max_length=100,null=True, blank=True)
    totalPage = models.CharField(max_length=100,null=True, blank=True)
    ratings = models.CharField(max_length=100,null=True, blank=True)
    image = models.CharField(max_length=250,null=True, blank=True)
    publishedDate = models.CharField(max_length=100,null=True, blank=True)
    pageRead = models.PositiveSmallIntegerField(null=True, blank=True,default=0)
    state = models.CharField(default='plan-to-read',max_length = 100, choices=[('completed','Completed'),('plan-to-read','Plan-to-Read'),('reading','Reading')])

