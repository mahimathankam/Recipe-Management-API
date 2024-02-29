from rtask.models import Recipe,Review
from rest_framework import serializers
from django.contrib.auth.models import User

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Recipe
        fields=['id','title','cuisine','mealtype','ingredients']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields=['id','recipe','user','rating','comments']

class  UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['id','username','password']
    def create(self, validated_data):
        u=User.objects.create_user(username=validated_data['username'],password=validated_data['password'])
        u.save()
        return u

