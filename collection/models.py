from django.db import models

# Create your models here. Database info happens here . See fields in Django docs 

class Band(models.Model):
    name = models.CharField(max_length=255) 
    description = models.TextField()
    slug = models.SlugField(unique=True)

#update here for database incorporation 

    # #contains information on how to read and write from a database 
    # a model in django is class that extends model.model and can pull information from a database. each dog model will represent one row of data 
    # class dog inherits the information from models.model

    #we have a model module that we are importing 
    #everytime we add somehting to our class we have to make migration :
        # manage.py makemigrations 
        # manage.py migrate   (look this up)
        # classes you will see a lot 
        # char 
        # int
        # float
        # boolean
        # text

# Example: 
#     class Animal:
#         def eat():

#     class Fish(animal):
#         def swim()

#         def breath_water():

#     class Anlerfish(Fish)
#         def glow(): 