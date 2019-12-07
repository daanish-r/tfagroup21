from django.http import HttpResponse
from django.forms import ModelForm
from django.shortcuts import render
from django.shortcuts import redirect

from .models import Fields
from .forms import SightingForm 

def index(request):
    return HttpResponse("Hello, this app lets you track squirrels and take a note")

def sighting_list(request, template_name='squirrel/all.html'):
    sightings = Fields.objects.all()
    context = {
            'sightings' : sightings,
    }
    return render(request, template_name, context)

def sighting_map(request, template_name='squirrel/map.html'):
    sightings = Fields.objects.order_by('?')[:100]
    context = {
            'sightings' : sightings,
            }
    return render(request, template_name, context)

def sighting_add(request, template_name='squirrel/add.html'):
    if request.method == 'POST':
        form = SightingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sighting_list')
    else: i
        form = SightingForm()
    
    context = {
        'form':form,
    }
    return render(request, template_name, context)

def sighting_update(request, pk, template_name='squirrel/sighting_form.html'):
    sighting = get_object_or_404(Sighting, pk=pk)
    form = SightingForm(request.POST or None, instance=sighting)
    if request.method=='POST' and 'update' in request.POST:
        if form.is_valid():
            form.save()
            return redirect('sighting_list')
    if request.method=='POST' and 'delete' in request.POST:
        sighting.delete()
        return redirect('sighting_list')
    return render(request, template_name, {'form':form})
