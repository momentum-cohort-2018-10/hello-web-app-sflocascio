from django.contrib import admin

# Register your models here.
from collection.models import Bands


class BandsAdmin(admin.ModelAdmin): 
    model = Bands
    list_display = ('name', 'description',) 
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Bands, BandsAdmin)