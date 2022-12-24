
from django.db import models
class comment(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    comment = models.CharField(max_length=400)
    activity_id = models.CharField(max_length=15)

class message(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    title = models.CharField(max_length=40)
    message = models.CharField(max_length=400)