from django.db import models
from django.contrib.postgres.fields import ArrayField


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

    class Meta: 
        verbose_name_plural = 'Product Type'

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

    class Meta: 
        verbose_name_plural = 'Skincare'

    # NORMAL_SKIN = "N"
    # DRY_SKIN = "D"
    # COMBINATION_SKIN = "C"
    # OILY_SKIN = "O"
    # SENSITIVE_SKIN = "S"

    # SKIN_TYPE = [
    #     ("NORMAL_SKIN", "Normal"),
    #     ("DRY_SKIN", "Dry"),
    #     ("COMBINATION_SKIN", "Combination"),
    #     ("OILY_SKIN", "Oily"),
    #     ("SENSITIVE_SKIN", "Sensitive"),
    # ]

    # ACNE = "A"
    # DARK_SPOTS = "DS"
    # ANTI_AGING = "AA"
    # WRINKLES = "W"
    # UNEVEN_SKIN_TONE = "UST"
    # TEXTURED_SKIN = "TS"
    # CONGESTION = "CG"
    # COMPROMISED_SKIN_BARRIER = "CSB"
    # SUN_DAMAGE = "SD"
    # BLACKHEADS = "BH"
    # ENLARGED_PORES = "EP"
    # OIL_CONTROL = "OC"
    # IRRITATION = "I"
    # RADIANCE = "R"
    # DULLNESS = "DU"
    # ROUGH_AND_BUMPY_SKIN = "RBS"
    # CALMING = "CA"
    # HYDRATION = "HY"
    # DRYNESS = "DR"
    # ECZEMA = "EC"

    # SKIN_CONCERN = [
    #     ("ACNE", "Acne"),
    #     ("DARK_SPOTS", "Dark Spots"),
    #     ("ANTI_AGING", "Anti-aging"),
    #     ("WRINKLES", "Wrinkles"),
    #     ("UNEVEN_SKIN_TONE", "Uneven Skin Tone"),
    #     ("TEXTURED_SKIN", "Textured Skin"),
    #     ("CONGESTION", "Congestion"),
    #     ("COMPROMISED_SKIN_BARRIER", "Compromised Skin Barrier"),
    #     ("SUN_DAMAGE", "Sun Damage"),
    #     ("BLACKHEADS", "Blackheads"),
    #     ("ENLARGED_PORES", "Enlarged Pores"),
    #     ("OIL_CONTROL", "Oil Control"),
    #     ("IRRITATION", "Irritation"),
    #     ("RADIANCE", "Radiance"),
    #     ("DULNESS", "Dullness"),
    #     ("ROUGH_AND_BUMPY_SKIN", "Rough & Bumpy Skin"),
    #     ("CALMING", "Calming"),
    #     ("HYDRATION", "Hydration"),
    #     ("DRYNESS", "Dryness"),
    #     ("ECZEMA", "Eczema"),
    # ]
    
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
    star_ingredient = ArrayField(
        models.CharField(max_length=500, default=list)
    )
    skin_type = ArrayField(
        models.CharField(max_length=200, default=list)
    )
    skin_concern = ArrayField(
        models.CharField(max_length=500, default=list)
    )

    # star_ingredient = models.CharField(max_length=500)
    # skin_type = models.CharField(max_length=500, choices=SKIN_TYPE)
    # skin_concern = models.CharField(max_length=500, choices=SKIN_CONCERN)
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
