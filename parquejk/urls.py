"""parquejk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from parquejkapp import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',                             TokenObtainPairView.as_view()),
    path('refresh/',                           TokenRefreshView.as_view()),
    path('verifyToken/',                       views.VerifyTokenView.as_view()),
    path('user/',                              views.UserCreateView.as_view()),
    path('plazas/',                            views.PlazasCreateView.as_view()),
    path('vehiculos/',                         views.VehiculosCreateView.as_view()),
    path('user/<int:pk>/',                     views.UserDetailView.as_view()),
    path('user/update/<int:pk>/',              views.UserUpdateView.as_view()),
    path('user/delete/<int:pk>/',              views.UserDeleteView.as_view()),
    path('user/other_accounts/<int:user_id>/', views.UserOtherAccounts.as_view()),
]
