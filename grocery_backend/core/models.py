from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)
    imageUrl = models.URLField(blank=False)

    def __str__(self) -> str:
        return self.title

    def __str__(self) -> str:
        return self.title
    
class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField(default=0, blank=False)
    description = models.TextField(max_length = 550)
    
    ratings = models.FloatField(blank=False, default=1.0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
   
    imageUrls = models.JSONField(blank=True)
    created_at = models.DateTimeField(default=timezone.now, blank=False)

    def __str__(self):
        return self.title