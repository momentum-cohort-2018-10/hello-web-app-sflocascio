from django.forms import ModelForm
from collection.models import Band

class BandForm(ModelForm):
    class Meta:
        model = Band
        fields = ('name', 'description',)


#If you were going the non-model route:
# from django import forms

# class SearchForm(form.Form):     (these are coming from models )
#     age = forms.ChoiceField(choices=DOG_AGE_CHOICES)
        # size = fomr.sMultipleChoiceField(choices=DOG_SIZE_CHOICES)
        # good_with_kids = forms.BooleanField(label="good with kids")

#to use this in your view you need to make an instance of it in your views 
#use a button tag <button type="submit>Search</button>"

#     Also need a form tag - needs a method and an action :
#         get. and post. are the two methods we use for forms 
#         use get when you have something repeatable that doesnt change anything 
#         use post - when you need to fill out a one time form, whenever your making a change in the database
#     <form method="GET" action="{% url '"
#     when you make a field in a form, it is required by default 
#     (what it looks like as a URL) -  localhost:8000/?age=young&size=1&

# THEN - you need to go to views to set this up :
#     def index(request):
#         if request.clean_field(self):
#             form = SearchForm(request.GET)
#             if form.is_valid():
#                     data = form.cleaned_data
#                     dogs = Dog.objects.filter(age=data['age'], size__in=data['size'])
#         else:
#             form= SearchForm()
#             dogs = Dog.objects.all()