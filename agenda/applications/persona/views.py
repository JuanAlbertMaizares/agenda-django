from multiprocessing import context
from pipes import Template
from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Person, Reunion
#rest framework
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView
)
from .serializers import (
    PersonSerializer, 
    PersonSerializer3, 
    PersonaSerializer, 
    PersonSerializer2, 
    ReunionSerializer, 
    ReunionSerializer2,
    ReunionSerializerLink
    ) 

class ListaPersonas(ListView):
    
    template_name = "persona/personas.html"
    context_object_name = 'personas'
    
    def get_queryset(self): 
        return Person.objects.all()
    
class PersonListApiView(ListAPIView):
    serializer_class = PersonSerializer
    def get_queryset(self):
        return Person.objects.all()
class PersonListView(TemplateView):
    template_name = 'persona/lista.html'

class PersonSearchApiView(ListAPIView):
    serializer_class = PersonSerializer
    
    def get_queryset(self):
        kword = self.kwargs['kword']
        return Person.objects.filter(
            full_name__icontains=kword
        )
class PersonCreateView(CreateAPIView):
    serializer_class = PersonSerializer
 
class PersonDetailView(RetrieveAPIView):
    serializer_class = PersonSerializer
    #queryset = Person.objects.filter(public = True)
    queryset = Person.objects.filter()
class PersonDeleteView(DestroyAPIView):
    serializer_class = PersonSerializer
    #queryset = Person.objects.filter(public = True)
    queryset = Person.objects.all()
class PersonUpdateView(UpdateAPIView):
    serializer_class = PersonSerializer 
    queryset = Person.objects.all()
class PersonModView(RetrieveUpdateAPIView):
    serializer_class = PersonSerializer 
    queryset = Person.objects.all()
    
class PersonApiLista(ListAPIView):
    #serializer_class = PersonaSerializer
    serializer_class = PersonSerializer3
    def get_queryset(self):
        return Person.objects.all()
class PersonApiLista2(ListAPIView):
    serializer_class = PersonSerializer2 
    def get_queryset(self):
        return Person.objects.all()
class ReunionApiLista(ListAPIView):
    
    #serializer_class = ReunionSerializer
    serializer_class = ReunionSerializer2
    def get_queryset(self):
        return Reunion.objects.all()
class ReunionApiListaLink(ListAPIView):
    
    #serializer_class = ReunionSerializer
    serializer_class = ReunionSerializerLink
    def get_queryset(self):
        return Reunion.objects.all()