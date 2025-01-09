from rest_framework import serializers
from .models import Recipe, Favorite
from django.contrib.auth.models import User

# Recipe Serializer
class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'

# User Serializer (for registering and authentication)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

# Favorite Serializer
class FavoriteSerializer(serializers.ModelSerializer):
    recipe_title = serializers.CharField(source='recipe.title', read_only=True)
    recipe_category = serializers.CharField(source='recipe.category', read_only=True)
    recipe_image = serializers.ImageField(source='recipe.image', read_only=True)

    class Meta:
        model = Favorite
        fields = '__all__'
