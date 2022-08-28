from django.shortcuts import render


def index(request):
    """ Renders index/home page """

    return render(request, 'home/index.html')