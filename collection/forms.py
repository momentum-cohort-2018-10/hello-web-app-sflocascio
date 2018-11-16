from django.forms import ModelForm
from collection.models import Band

class BandForm(ModelForm):
    class Meta:
        model = Band
        fields = ('name', 'description',)


        