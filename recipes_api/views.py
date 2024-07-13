from django.shortcuts import render
from rest_framework import generics
from .serializers import RecipeSerializer
from .models import Recipes

# Create your views here.
class RecipeList(generics.ListCreateAPIView):
    queryset = Recipes.objects.all().order_by('id')
    serializer_class = RecipeSerializer

class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipes.objects.all().order_by('id')
    serializer_class = RecipeSerializer