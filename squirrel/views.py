from django.http import HttpResponse

from .models import Pet

def all_pets(request):
    terxt = ''
    pets = Pet.objects.all()
    for pet in pets:
        text += pet.name + ', '
        return HttpResponse(text)

def pet_details(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    return HttpResponse(pet.name)
