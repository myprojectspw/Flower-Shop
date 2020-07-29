from django.db import models

class Flower(models.Model):
    name = models.CharField(max_length=120)
    color = models.TextField()

    def __str__(self):
        return self.name