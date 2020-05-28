from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images')
    url = models.URLField(blank=True)


class Resume(models.Model):
    year = models.CharField(max_length=10)
    degree = models.CharField(max_length=100)
    institute = models.CharField(max_length=100)
    description = models.CharField(max_length=250)