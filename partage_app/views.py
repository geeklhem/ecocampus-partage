from django.shortcuts import render
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
    return HttpResponseRedirect("/","OK.")

def remove(request):
    obj = models.Shareable.objects.get(id=request.POST["obj"])
    obj.delete()
    return HttpResponseRedirect("/","OK.")
