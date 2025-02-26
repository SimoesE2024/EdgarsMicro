# views.py
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import SolicitationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


@login_required(login_url='/login/')
def home(request):
    return render(request, '_base.html')

class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = '_base.html'
    login_url = '/login/'  # Redireciona para a página de login
    redirect_field_name = 'next'  # Redireciona de volta após login
# Página de registro
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")  # Redireciona após cadastro
    else:
        form = UserCreationForm()
    
    return render(request, "register.html", {"form": form})

# Página inicial protegida por login
@login_required
def home(request):
    return render(request, "index.html")  # Certifique-se de ter este template

def solicitar_credito(request):
    if request.method == 'POST':
        form = SolicitationForm(request.POST)
        if form.is_valid():
            # Dados do formulário
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            amount = form.cleaned_data['amount']
            installments = form.cleaned_data['installments']
            collateral = form.cleaned_data['collateral']

            # Compor o corpo do e-mail
            message = (
                f"Nome: {name}\n"
                f"Email: {email}\n"
                f"Telefone: {phone}\n"
                f"Valor Solicitado: {amount}\n"
                f"Número de Parcelas: {installments}\n"
                f"Bem a Penhorar: {collateral}"
            )
            
    
            # Enviar o e-mail
            send_mail(
                'Solicitação de Crédito Pagamentos Diários',
                message,
                settings.DEFAULT_FROM_EMAIL,
                ['edgarsimoes52@gmail.com'],  # Email para onde a solicitação será enviada
                fail_silently=False,
            )
            # Redirecionar para a página inicial ou página de agradecimento
            return redirect('home')
    else:
        form = SolicitationForm()

    return render(request, 'solicitar_credito.html', {'form': form})


