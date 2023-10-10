from django.db import models

# Create your models here.

class Shirt(models.Model):
    title = models.CharField(max_length= 70)
    price = models.PositiveIntegerField()
    brand = models.CharField(max_length= 50, null=True)
    description = models.TextField(blank=True)
    is_bestseller = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"

class Brand(models.Model):
    title = models.CharField(max_length= 70)
    logo = models.ImageField()

    def __str__(self):
        return f"{self.title}"

class Product(models.Model):
    title = models.CharField(max_length= 70)
    description = models.TextField()
    category = models.CharField(max_length= 50)
    image = models.ImageField(blank= True, upload_to='product-img')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    price = models.PositiveIntegerField()
    slug = models.SlugField(blank=True)
    is_bestseller = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.slug = self.id
        super().save(*args, **kwargs)