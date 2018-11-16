from django.contrib import admin

# Register your models here.
from collection.models import Band


class BandAdmin(admin.ModelAdmin): 
    model = Band
    list_display = ('name', 'description',) 
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Band, BandAdmin)


#admin is a way to interface with the models youve built .. models need to be built first 