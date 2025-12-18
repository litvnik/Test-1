from django.db import models

# Create your models here.
class Mammal(models.Model):
    name = models.CharField(max_length=100)
    habitat = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.habitat})"

class Bird(models.Model):
    name = models.CharField(max_length=100)
    habitat = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.habitat})"