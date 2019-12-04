from django.http import HttpResponse
from django.forms import ModelForm

from .models import Fields

def index(request):
    return HttpResponse("Hello, this app lets you track squirrels and take a note")


class SightingForm(ModelForm):
    class Meta:
        model = Fields
        fields = '__all__'

def sighting_list(request, template_name='squirrel/all.html'):
    sightings = Sighting.objects.all()
    context = {
            'sightings' : sightings,
    }
    return render(request, template_name, context)

def sighting_map(request, template_name='squirrel/map.html'):
    sightings = Sighting.objects.order_by('?')[:100]
    context = {
            'sightings' : sightings,
    }
    return render(request, template_name, context)
