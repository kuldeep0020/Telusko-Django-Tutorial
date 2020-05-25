from django.shortcuts import render
from .models import Destination


# Create your views here.
def index(request):

    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = "Mumbai in India."
    dest1.price = 700

    dest2 = Destination()
    dest2.name = 'Delhi'
    dest2.desc = 'Polluted City.'
    dest2.price = 700

    dest3 = Destination()
    dest3.name = 'Kerala'
    dest3.desc = 'Green City.'
    dest3.price = 700

    return render(request, 'index.html', {'dest1': dest1, 'dest2': dest2, 'dest3': dest3})
