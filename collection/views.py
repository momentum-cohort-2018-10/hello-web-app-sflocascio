from django.shortcuts import render, redirect
from collection.forms import BandForm
from collection.models import Band
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.http import Http404


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

@login_required
def edit_band(request, slug):
        band = Band.objects.get(slug=slug)
        if band.user != request.user: 
                raise Http404
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

def create_band(request):
        form_class = BandForm
        if request.method == 'POST':
                form = form_class(request.POST)
                if form.is_valid():
                        band = form.save(commit=False)
                        band.user = request.user
                        band.slug = slugify(band.name)
                        band.save()
                        return redirect('band_detail', slug=band.slug)
        else:
             form = form_class()

        return render(request, 'bands/create_band.html', { 'form': form,
})

def browse_by_name(request, initial=None): 
        if initial:
                bands = Band.objects.filter(
                        name__istartswith=initial).order_by('name')
        else:
                bands = Band.objects.all().order_by('name')
        return render(request, 'search/search.html', { 
                'bands': bands,
                'initial': initial,
})



#Two scoops of Django - book that clinton recommends 
# excercises in programming style 
# 