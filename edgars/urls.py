from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('usuarios/', include('django.contrib.auth.urls')),  # Adiciona todas as URLs de autenticação do Django
]
