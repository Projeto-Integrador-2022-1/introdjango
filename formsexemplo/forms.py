from django import forms
from django.core.validators import RegexValidator

from polls.models import Questao

class FalaAihForm(forms.Form):
    cpf = forms.CharField(
        label="CPF",
        widget=forms.TextInput(attrs={"class": "form-control", "pattern": "[0-9]{3}[.]?[0-9]{3}[.]?[0-9]{3}[-]?[0-9]{2}"}),
        required=True,
        validators=[
            RegexValidator(regex='[0-9]{3}[.]?[0-9]{3}[.]?[0-9]{3}[-]?[0-9]{2}')
            ])
    nascimento = forms.DateField(
        label="Data de nascimento:",
        required=True,
        widget=forms.DateInput(
            attrs={"class": "form-control" }
        ),
    )
    email = forms.EmailField(
        label="E-mail",
        required=False,
        widget=forms.EmailInput(
            attrs={"class": "form-control"}
        )
    )
    preferida = forms.ModelChoiceField(
        label="Sua questão preferida foi: ",
        queryset=Questao.objects.filter(pk__gt=1),
        widget= forms.RadioSelect(
        )
    )


class NovaQuestao(forms.ModelForm):
    class Meta:
        model = Questao
        fields = ["questao_texto"]