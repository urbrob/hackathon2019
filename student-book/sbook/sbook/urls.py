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
from notes import views
from forms import LoginForms
from django.conf.urls import url


from django.conf.urls import url
from oauth2_provider import views as oauth2_views

from accounts import views as account_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("notes.urls")),
    path('login/', auth_view.LoginView.as_view(), {'authentication_form':LoginForms}, name='login'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url('app/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('register/', account_views.UserRegister.as_view(), name='register'),
    path('logout', account_views.logout, name='logout')
]
