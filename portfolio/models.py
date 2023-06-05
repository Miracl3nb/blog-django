from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField


# Create your models here.
class Project(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=500)
    image = ImageField(upload_to='portfolio/images')
    url = URLField(blank=True)

#https://www.youtube.com/watch?v=zBjMF6je24U&t=1353s
