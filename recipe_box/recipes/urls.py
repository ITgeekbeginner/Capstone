from django.urls import path
from .views import FavoriteRecipe, RemoveFavoriteRecipe, ListFavoriteRecipes
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('recipes/', views.RecipeListCreate.as_view(), name='recipe-list-create'),
    path('recipes/<int:pk>/', views.RecipeRetrieveUpdateDelete.as_view(), name='recipe-retrieve-update-delete'),
    path('recipes/category/', views.RecipeCategoryList.as_view(), name='recipe-category-list'),
    path('recipes/ingredient/', views.RecipeIngredientList.as_view(), name='recipe-ingredient-list'),
    path('favorites/', ListFavoriteRecipes.as_view(), name='list-favorites'),
    path('favorites/add/', FavoriteRecipe.as_view(), name='add-favorite'),
    path('favorites/remove/', RemoveFavoriteRecipe.as_view(), name='remove-favorite'),
]
