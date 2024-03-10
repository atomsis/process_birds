from django.db import models
from django.shortcuts import redirect


class Bird(models.Model):
    name = models.CharField(max_length=100)
    feather_color = models.CharField(max_length=50)
    image = models.ImageField(upload_to='bird_images/')

    def __str__(self):
        return self.name


class BirdSighting(models.Model):
    bird = models.ForeignKey(Bird, on_delete=models.CASCADE)
    sighting_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.bird.name} sighting at {self.sighting_time}"