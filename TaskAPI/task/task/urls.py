"""
URL configuration for task project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rtask import views
from rest_framework.authtoken import views as rviews
from rest_framework.routers import SimpleRouter
router=SimpleRouter()
router.register("reg",views.CreateUser)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.recipelist.as_view(),name='recipelist'),
    path("detail/<int:pk>",views.recipedetail.as_view(),name='recipedetail'),
    path("register/",include(router.urls)),
    path('api-auth-token/', rviews.obtain_auth_token),
    path('logout',views.user_logout.as_view(),name='logout'),
    # path('reviewview',views.reviewview.as_view(),name='view'),
    path("reviewadd/<int:pk>",views.reviewadd.as_view(),name='reviewadd'),
    path("reviewdetail/<int:pk>",views.reviewdetail.as_view(),name='reviewdetail'),
    path('search',views.search.as_view(),name='search'),

]
