from django.views.generic import TemplateView
from django.shortcuts import render

# Views baseadas em classe
class HomePageView(TemplateView):
    template_name = 'index.html'  # Este está na pasta templates/

class CreditoDiarioView(TemplateView):
    template_name = 'registration/credito_diario.html'  # Corrigido para templates/registration/

class CreditoRelampagoView(TemplateView):
    template_name = 'registration/credito_relampago.html'  # Corrigido para templates/registration/

class CreditoPlusView(TemplateView):
    template_name = 'registration/credito_plus.html'  # Corrigido para templates/registration/
    
class CreditoEmpresaView(TemplateView):
    template_name = 'registration/credito_empresa.html'  # Corrigido para templates/registration/

# Views baseadas em função
def signup(request):
    return render(request, 'signup.html')


def home(request):
    return render(request, 'index.html')

def credito_diario_view(request):
    return render(request, 'registration/credito_diario.html')

def credito_relampago(request):
    return render(request, 'registration/credito_relampago.html')

def credito_plus(request):
    return render(request, 'registration/credito_plus.html')

def credito_empresa(request):
    return render(request, 'registration/credito_empresa.html')