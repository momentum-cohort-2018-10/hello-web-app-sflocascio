from django.shortcuts import render
from collection.models import Bands


def index(request):
    number = 6
    Bandss = Bands.objects.all()
    return render(request, 'index.html', {
        'number': number,
        'Bandss': Bandss,
    })