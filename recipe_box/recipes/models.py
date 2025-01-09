from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY_CHOICES = [
    ('Dessert', 'Dessert'),
    ('Main Course', 'Main Course'),
    ('Breakfast', 'Breakfast'),
    ('Vegetarian', 'Vegetarian'),
    ('Mocktail', 'Mocktail'),
    ('Appetizer', 'Appetizer'),
    ('Side Dish', 'Side Dish'),
    ('Soup', 'Soup'),
    ('Salad', 'Salad'),
    ('Bread', 'Bread'),
    ('Sauce', 'Sauce'),
    ('Snack', 'Snack'),
]

# Recipe Model
class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    ingredients = models.TextField()  # Store ingredients as a text list
    instructions = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    preparation_time = models.IntegerField()  # in minutes
    cooking_time = models.IntegerField()  # in minutes
    servings = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='recipes', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='recipe_images/', null=True, blank=True)

    def __str__(self):
        return self.title

# Favorite Model
class Favorite(models.Model):
    user = models.ForeignKey(User, related_name='favorites', on_delete=models.CASCADE)
    recipe = models.ForeignKey('Recipe', related_name='favorited_by', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'recipe')  # Prevent multiple favorites for the same recipe by the same user

    def __str__(self):
        return f"{self.user.username} - {self.recipe.title} as favorite"