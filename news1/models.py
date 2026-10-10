from django.db import models

class News1Model(models.Model):
    title = models.CharField(max_length=100)
    body= models.TextField()


# Create your models here.
