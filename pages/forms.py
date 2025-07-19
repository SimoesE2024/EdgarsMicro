from django import forms

class SolicitationForm(forms.Form):
    name = forms.CharField(max_length=100, label='Nome Completo')
    email = forms.EmailField(label='Email')
    phone = forms.CharField(max_length=15, label='Telefone')
    amount = forms.IntegerField(label='Valor Solicitado')
    installments = forms.IntegerField(
        label='Número de Parcelas', min_value=1, max_value=36
    )
    collateral = forms.CharField(max_length=200, label='Bem a Penhorar')

    # NOVOS CAMPOS DE UPLOAD
    document_bi = forms.FileField(label='Cópia do BI', required=True)
    document_income = forms.FileField(label='Declaração de Rendimento', required=True)
    photo_collateral = forms.ImageField(label='Foto do Bem a Penhorar', required=True)

    def clean_amount(self):
        amount = self.cleaned_data.get("amount")
        if amount > 5000:
            raise forms.ValidationError("O valor máximo permitido é 5.000!")
        return amount
