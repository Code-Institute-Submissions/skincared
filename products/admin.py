from django.contrib import admin
from .models import Brand, ProductType


class BrandAdmin(admin.ModelAdmin):
    """ Customise Brand Admin Panel """

    list_display = (
        'friendly_name',
        'name'
    )

    ordering = ('friendly_name',)


class ProductTypeAdmin(admin.ModelAdmin):
    """ Customise Product Type Admin Panel """

    list_display = (
        'friendly_name',
        'name'
    )

    ordering = ('friendly_name',)


admin.site.register(Brand, BrandAdmin)
admin.site.register(ProductType, ProductTypeAdmin)
