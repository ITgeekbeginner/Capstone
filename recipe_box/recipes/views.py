from django.shortcuts import render
from rest_framework import generics, permissions, filters
from .models import Recipe, Favorite
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import RecipeSerializer, FavoriteSerializer
from .pagination import RecipePagination
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
from django.http import JsonResponse
from django.contrib.auth.models import User

# Create your views here.

# List or Create Recipes (public)
class RecipeListCreate(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    pagination_class = RecipePagination
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = ['preparation_time', 'cooking_time', 'servings', 'created_date']  # Fields available for sorting
    ordering = ['preparation_time']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # allow unauthenticated to view

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Retrieve, Update, Delete a Recipe (only owners can update/delete)
class RecipeRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self):
        obj = super().get_object()
        if obj.user != self.request.user:
            raise permissions.PermissionDenied("You can only edit or delete your own recipes.")
        return obj

# List Recipes by Category
class RecipeCategoryList(generics.ListAPIView):
    serializer_class = RecipeSerializer

    def get_queryset(self):
        category = self.request.query_params.get('category', None)
        return Recipe.objects.filter(category=category)

# List Recipes by Ingredient
class RecipeIngredientList(generics.ListAPIView):
    serializer_class = RecipeSerializer

    def get_queryset(self):
        ingredient = self.request.query_params.get('ingredient', None)
        return Recipe.objects.filter(ingredients__icontains=ingredient)

class RecipeFilter(generics.ListAPIView):
    serializer_class = RecipeSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ['category', 'preparation_time', 'cooking_time', 'servings']
    ordering_fields = ['preparation_time', 'cooking_time']

# Add a Recipe to Favorites
class FavoriteRecipe(generics.CreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Ensure that the user can only favorite a recipe once
        recipe = self.request.data.get('recipe')
        if Favorite.objects.filter(user=self.request.user, recipe=recipe).exists():
            raise serializers.ValidationError("You have already favorited this recipe.")
        serializer.save(user=self.request.user)

# Remove a Recipe from Favorites
class RemoveFavoriteRecipe(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        recipe_id = request.data.get('recipe')
        try:
            favorite = Favorite.objects.get(user=request.user, recipe_id=recipe_id)
            favorite.delete()
            return JsonResponse({"message": "Recipe removed from favorites."}, status=200)
        except Favorite.DoesNotExist:
            return JsonResponse({"error": "Recipe not found in favorites."}, status=404)

# List All Favorite Recipes for the Authenticated User
class ListFavoriteRecipes(generics.ListAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)