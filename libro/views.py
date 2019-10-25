from django.shortcuts import render
from rest_framework import generics
from .models import Libro
from .serializer import LibroSerializer

# Create your views here.
class LibroList(generics.ListCreateAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer