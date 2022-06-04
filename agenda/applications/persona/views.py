from multiprocessing import context
from pipes import Template
from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Person
#rest framework
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView
)
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