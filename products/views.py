from django.shortcuts import render
from .models import Brand


def brands(request):
    """ Renders all brands, sorting and serach queries """

    brands = Brand.objects.all()

    context = {
        'brands': brands, 
    }

    return render(request, 'brands/brands.html', context)