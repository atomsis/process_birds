from django.db import models
from django.shortcuts import redirect


class Bird(models.Model):
    name = models.CharField(max_length=100)
    feather_color = models.CharField(max_length=50)
    image = models.ImageField(upload_to='bird_photos', null=True, blank=True)

    def __str__(self):
        return self.name


class BirdSaw(models.Model):
    bird = models.ForeignKey(Bird, on_delete=models.CASCADE)
    saw = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.bird.name} sighting at {self.saw}"