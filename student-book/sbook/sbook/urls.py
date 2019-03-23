"""sbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib.auth import views as auth_view
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
<<<<<<< HEAD
=======
from notes import views
>>>>>>> 2d7a756fd1ca95f5729b45703006fbd34b90c918

from forms import LoginForms

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    #path("api/", include("notes.urls")),
=======
    path("api/", include("notes.urls")),
>>>>>>> 2d7a756fd1ca95f5729b45703006fbd34b90c918
    path('login/', auth_view.LoginView.as_view(), {'authentication_form':LoginForms}),
    path('', TemplateView.as_view(template_name='home.html'))
]
