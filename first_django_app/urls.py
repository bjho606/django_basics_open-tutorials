"""first_django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from first_django_app import views

urlpatterns = [
    path('', views.index),           # 사용자가 홈으로 들어왔다 (아무것도 없는 경로로 들어옴)
    path('create/', views.create),    # 사용자가 create로 들어왔다
    path('read/<id>/', views.read)     # 사용자가 read/<id>으로 들어왔다
]
