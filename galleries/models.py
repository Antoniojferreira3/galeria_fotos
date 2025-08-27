# recipes/models.py
from django.db import models

class galery(models.Model):
    title = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()
    cooking_time = models.IntegerField(help_text="Em minutos")

def __str__(self):
    return self.title