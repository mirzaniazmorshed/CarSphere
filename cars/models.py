from django.db import models

from brands.models import BrandModel

# Create your models here.
class CarModel(models.Model):
    name = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    brand = models.ForeignKey(BrandModel, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='cars/media/uploads/', blank=True, null=True)
    description = models.TextField()
    
    def __str__(self) -> str:  
        return self.name


class CommentModel(models.Model):
      post = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='comments')
      name = models.CharField(max_length=50)
      email = models.EmailField(unique=True)
      body  = models.TextField()
      created_on = models.DateTimeField(auto_now_add=True)

      def __str__(self) -> str:
           return f"Comments by {self.name}"
      