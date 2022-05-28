from multiprocessing import context
from django.shortcuts import render
from django.views.generic import ListView 
from .models import Person
#rest framework
from rest_framework.generics import ListAPIView
from .serializers import PersonSerializer

class ListaPersonas(ListView):
    
    template_name = "persona/personas.html"
    context_object_name = 'personas'
    
    def get_queryset(self): 
        return Person.objects.all()
    
class PersonListApiView(ListAPIView):
    serializer_class = PersonSerializer
    def get_queryset(self):
        return Person.objects.all()