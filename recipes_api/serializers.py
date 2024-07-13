from rest_framework import serializers
from .models import Recipes

#Serializer
class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipes
        fields = ('id', 'name', 'main_ingredient', 'origin', 'popularity')