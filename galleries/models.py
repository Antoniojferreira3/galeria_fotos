# galleries/models.py
from django.db import models

class Galery(models.Model):
    title = models.CharField(max_length=200)
    photo_location = models.TextField()
    comments = models.TextField()
    photo_period = models.IntegerField(help_text="Em dias")

    image = models.ImageField(upload_to='galleries/', blank=True, null=True)


    def __str__(self):
        return self.title
    
    class Meta:
# Define o nome da tabela no plural para o painel de administração
        verbose_name_plural = "galleries"