from django import forms
from pages.forms import SolicitationForm

class SolicitationForm(forms.Form):
    name = forms.CharField(max_length=100, label='Nome Completo')
    email = forms.EmailField(label='Email')
    phone = forms.CharField(max_length=15, label='Telefone')
    amount = forms.IntegerField(label='Valor Solicitado')
    installments = forms.IntegerField(label='Número de Parcelas', min_value=1, max_value=36)
    collateral = forms.CharField(max_length=200, label='Bem a Penhorar')

    # Campos obrigatórios adicionais
    document_bi = forms.FileField(label='Documento de Identidade')
    document_income = forms.FileField(label='Comprovante de Renda')
    photo_collateral = forms.FileField(label='Foto do Bem a Penhorar')

    def clean_amount(self):
        amount = self.cleaned_data.get("amount")
        if amount > 5000:
            raise forms.ValidationError("O valor máximo permitido é 5.000!")
        return amount

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        if not phone.isdigit():
            raise forms.ValidationError("O telefone deve conter apenas números.")
        return phone
