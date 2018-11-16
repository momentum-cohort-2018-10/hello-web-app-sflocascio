from django.shortcuts import render, redirect
from collection.forms import BandForm
from collection.models import Band


def index(request):
    number = 6
    bands = Band.objects.all()
    return render(request, 'index.html', {
        'number': number,
        'bands': bands,
    })

def band_detail(request, slug):
    band = Band.objects.get(slug=slug)
    return render(request, 'bands/band_detail.html', {            
        'band': band,
})

def edit_band(request, slug):
        band = Band.objects.get(slug=slug)
        form_class = BandForm
        if request.method == "POST":
                form = form_class(data=request.POST, instance=band)
                if form.is_valid():
                        form.save()
                        return redirect('band_detail', slug=band.slug)
        else:
                form = form_class(instance=band)
        return render(request, 'bands/edit_band.html', {
                'band': band,
                'form': form,
        })
