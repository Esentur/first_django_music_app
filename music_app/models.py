
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
 
class Category(models.Model):
    title = models.SlugField(primary_key=True)
    def __str__(self) -> str:
        return self.title

class Music(models.Model):
    def __str__(self) -> str:
        return f'{self.title} - {self.category}'
    COUNTRY =(
        ('KG','Kyrgyzstan'),
        ('KZ', 'Kazakhstan')
    )
    author = models.ManyToManyField(User)

    title = models.CharField(max_length=50)
    description =models.TextField(null=True, blank = True) # обычно прописывается в паре. дает возможность не заполнять формочку.
    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name = "music")
    duration = models.IntegerField()
    country = models.CharField(max_length=30, choices=COUNTRY)
    created_at = models.DateField(auto_now_add=True)

