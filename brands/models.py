from django.db import models

# Create your models here.
class BrandModel(models.Model):
    brand_name = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.brand_name
    
