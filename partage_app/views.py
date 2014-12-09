#-*-coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse,  HttpResponseRedirect
from django.template import RequestContext, loader
from partage_app import models
from django.utils import timezone

def index(request,msg=None,sort="category"):
    loc = models.Location.objects.all()
    categories = models.Category.objects.all()
    shareables = {} 
    
    context = {"locations":loc, 
               "categories":categories,
               "sort":sort,
               "msg":msg,
    }
    
    return render(request, 'partage_app/index.html', context)
    
def add(request):
    obj = models.Shareable(name=request.POST["name"],
                           details=request.POST["details"],
                           category=models.Category.objects.get(id=request.POST["category"]),
                           location=models.Location.objects.get(id=request.POST["location"]),
                           added=timezone.now(),
                           owner=models.User.objects.get(id=request.POST["user"]),
                           classe=request.POST["classe"],
    )
    obj.save()
    #return index(request)
    return HttpResponseRedirect(reverse('partage:index'))
    #return HttpResponseRedirect(".","OK.")

def remove(request):
    obj = models.Shareable.objects.get(id=request.POST["obj"])
    obj.delete()
    #return HttpResponseRedirect(".","OK.")
    #return render(reverse('partage:index'))
    return HttpResponseRedirect(reverse('partage:index'))

def edit(request, obj_id):
    obj = get_object_or_404(models.Shareable, id=obj_id)
    if request.method == "POST":
        user = models.User.objects.get(id=request.POST["user"])
        if obj.owner != user: # do checks again
            return HttpResponse("Il semblerait que vous ne soyez pas le propriétaire de l'objet en question...")
        obj.details = request.POST["details"]
        obj.name = request.POST["name"]
        obj.save()
        return HttpResponseRedirect(reverse('partage:index'))
        
    elif request.method == "GET":

        loc = models.Location.objects.all()
        categories = models.Category.objects.all()
    
        context = {"locations":loc, 
                   "categories":categories,
                   "obj":obj,
                   "owner": str(obj.owner)
                   }

        return render(request, 'partage_app/edit.html', context)
    #return HttpResponseRedirect(reverse('partage:index'))
