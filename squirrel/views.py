from django.http import HttpResponse

from .models import Fields

def index(request):
    return HttpResponse("Hello, this app lets you track squirrels and take a note")
