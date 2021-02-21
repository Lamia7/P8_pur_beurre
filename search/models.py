from django.db import models

from users.models import User


class Category(models.Model):
    """Represents the category table"""

    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    """Represents the product table"""

    name = models.CharField(max_length=150, unique=True)
    brands = models.CharField(max_length=150)
    barcode = models.BigIntegerField(unique=True)
    url = models.URLField()
    image_url = models.URLField()
    nutriscore = models.CharField(max_length=1)
    energy_100g = models.FloatField(default=0, blank=True)  # can be empty
    sugars_100g = models.FloatField(default=0, blank=True)
    sodium_100g = models.FloatField(default=0, blank=True)
    fat_100g = models.FloatField(default=0, blank=True)
    salt_100g = models.FloatField(default=0, blank=True)
    categories = models.ManyToManyField(Category, related_name='categories')

    def __str__(self):
        return f"{self.name}, {self.nutriscore}"

class Favorite(models.Model):
    """Represents the favorite table
    relation plusieurs à un
    product: lié à un produit par ForeignKey. 1 pdt peut être dans pls lignes favoris
    substitute: peut avoir un seul produit
    """

    # CASCADE:if is deleted in Products'table, will be deleted here NOT the opposite
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="favorite_product")  
    substitute = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="favorite_substitute")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favorite_user")

    def __str__(self):
        return f"Produit: {self.product}, Substitut: {self.substitute}"
