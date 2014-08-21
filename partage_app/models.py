from django.db import models
from django.contrib.auth.models import User

class Location(models.Model):
    """ One of the ENS buildings"""
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200)
    color =  models.CharField(max_length=9)

    def __unicode__(self):
        return self.name

class Shareable(models.Model):
    """ An object thar can be shared """
    


    NEED = 'demande'
    OFFER = 'propose'
    CLASS_CHOICES = (
        (NEED, 'demande'),
        (OFFER, 'propose'),
    )
    
    classe = models.CharField(max_length=10,
                              choices=CLASS_CHOICES,
                              default=NEED)

    name = models.CharField(max_length=200)
    
    details = models.CharField(max_length=1000)
    added = models.DateTimeField("date d'ajout")
    owner = models.ForeignKey(User)
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return self.name
