from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import HomePageView, register, solicitar_credito
from edgars import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # 🔹 Mantemos apenas a `HomePageView` na raiz, exigindo login
    path('', HomePageView.as_view(), name='home'),

    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),

    
    path('pages/signup/', views.register, name='register'),
    path('solicitar/', solicitar_credito, name='solicitar_credito'),

    # 🔹 Apenas inclua as URLs do 'pages' se forem necessárias
    path('pages/', include('pages.urls')),
]
