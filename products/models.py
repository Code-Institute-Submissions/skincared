from django.db import models


class Brand(models.Model):
    """ Brands Model """
    name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=200, null=True, blank=True)
    about = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def brand_friendly_name(self):
        """ Returns Brands User Friendly Name """
        return self.friendly_name


class ProductType(models.Model):
    """ Product Type Model """
    name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=200, null=True, blank=True)
    about = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def product_type_friendly_name(self):
        """ Returns Product Type User Friendly Name """

        return self.friendly_name


class Skincare(models.Model):
    """ Skincare Products Model """
    NORMAL_SKIN = "N"
    DRY_SKIN = "D"
    COMBINATION_SKIN = "C"
    OILY_SKIN = "O"
    SENSITIVE_SKIN = "S"

    SKIN_TYPE = [
        ("NORMAL_SKIN", "Normal"),
        ("DRY_SKIN", "Dry"),
        ("COMBINATION_SKIN", "Combination"),
        ("OILY_SKIN", "Oily"),
        ("SENSITIVE_SKIN", "Sensitive"),
    ]

    brand = models.ForeignKey(
        'Brand', null=True, blank=True, on_delete=models.SET_NULL
        )
    about = models.TextField()
    name = models.CharField(max_length=350)
    quantity = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField()
    directions = models.TextField()
    ingredients = models.TextField()
    product_type = models.ForeignKey(
        'ProductType', null=True, blank=True, on_delete=models.SET_NULL
        )
    product_subtype = models.CharField(max_length=150)
    # star_ingredient = models.CharField(max_length=500)
    skin_type = models.CharField(max_length=500, choices=SKIN_TYPE)
    # skin_concern = models.CharField(max_length=500)
    cruelty_free = models.CharField(max_length=10)
    vegan = models.CharField(max_length=10)
    alcohol_free = models.CharField(max_length=10)
    fragrance_free = models.CharField(max_length=10)
    sku = models.CharField(max_length=300, null=True, blank=True)
    rating = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
        )

    def __str__(self):
        return self.name
