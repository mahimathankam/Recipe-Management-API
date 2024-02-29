from django.shortcuts import render
from rtask.models import Recipe,Review
from django.contrib.auth.models import User
from rtask.serializers import RecipeSerializer,ReviewSerializer,UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,viewsets
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

class recipelist(APIView):
    def get(self,request):
        r=Recipe.objects.all()
        rec=RecipeSerializer(r,many=True)
        return Response(rec.data)
    def post(self,request):
        rec=RecipeSerializer(data=request.data)
        if rec.is__valid():
            rec.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class recipedetail(APIView):
    def get(self,request,pk):
        r=Recipe.objects.get(pk=pk)
        rec=RecipeSerializer(r)
        return Response(rec.data)
    def put(self,request,pk):
        r = Recipe.objects.get(pk=pk)
        rec=RecipeSerializer(r,data=request.data)
        if rec.is__valid():
            rec.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        r=Recipe.objects.get(pk=pk)
        r.delete()
        return Response(status=status.HTTP_200_OK)

class CreateUser(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class user_logout(APIView):
    permission_classes = [IsAuthenticated, ]
    def get(self,request):
        self.request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

# class reviewview(APIView):
#     permission_classes = [IsAuthenticated,]
#     def get(self,request):
#         u = self.request.user
#         r = Review.objects.filter(user=u)
#         rev=ReviewSerializer(r,many=True)
#         return Response(rev.data)


class reviewadd(APIView):
    permission_classes = [IsAuthenticated,]
    def post(self,request,pk):
        try:
            r = Recipe.objects.get(pk=pk)
            u = self.request.user
            rating=request.data.get('rating')
            comments=request.data.get('comments')
            rev=Review.objects.create(recipe=r,user=u,rating=rating,comments=comments)
            rev.save()
            return Response(status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class reviewdetail(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self,request,pk):
        r=Recipe.objects.get(pk=pk)
        review=Review.objects.filter(recipe=r)
        rev=ReviewSerializer(review,many=True)
        return Response(rev.data)

class search(APIView):
    def get(self,request):
        query=self.request.query_params.get('search')
        if (query):
            r=Recipe.objects.filter(Q(title__icontains=query) | Q(cuisine__icontains=query) | Q(mealtype__icontains=query))
            rec=RecipeSerializer(r,many=True)
            return Response(rec.data)