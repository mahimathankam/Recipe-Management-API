from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    title=models.CharField(max_length=30)
    cuisine=models.CharField(max_length=30)
    mealtype=models.CharField(max_length=30)
    ingredients=models.TextField()
    def __str__(self):
        return self.title

class Review(models.Model):
    recipe=models.ForeignKey(Recipe,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.IntegerField()
    comments=models.TextField()
    def __str__(self):
        return self.recipe.title