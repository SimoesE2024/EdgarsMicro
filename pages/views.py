from django.views.generic import TemplateView
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import SolicitationForm  # Importação correta
from django.contrib import messages

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


def solicitar_credito(request):
    if request.method == 'POST':
        form = SolicitationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            amount = form.cleaned_data['amount']
            collateral = form.cleaned_data['collateral']

            message = f"Nome: {name}\nEmail: {email}\nTelefone: {phone}\nValor Solicitado: {amount}\nBem a Penhorar: {collateral}"
            
            send_mail(
                'Solicitação de Crédito Pagamentos Diários',
                message,
                settings.DEFAULT_FROM_EMAIL,
                ['edgarsimoes52@gmail.com'],  
                fail_silently=False,
            )
            return redirect('home')
    else:
        form = SolicitationForm()

    return render(request, 'solicitar_credito.html', {'form': form})