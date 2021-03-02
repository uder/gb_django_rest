from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Author
from .serializers import AutorModelSerializer

class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AutorModelSerializer

# Create your views here.
