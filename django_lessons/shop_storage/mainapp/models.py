from django.db import models


class StorageItem(models.Model):
    name = models.CharField(max_length=64, unique=True)
    image = models.ImageField(upload_to='product_images')
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
