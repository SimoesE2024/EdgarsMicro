from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views  # Importando o módulo views
from .views import HomePageView
#from pages.views import CreditoDiarioView, CreditoPlusView, CreditoRelampagoView, HomePageView, signup


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('usuarios/', include('django.contrib.auth.urls')),  # Adiciona todas as URLs de autenticação do Django
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', HomePageView.as_view(), name='home'),
     
]
