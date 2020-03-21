from django import forms
from .models import Citizen


class CitizenForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(),
                                 label="Vorname",
                                 help_text="Bitte geben sie ihren vollständigen Vornamen ein")
    last_name = forms.CharField(widget=forms.TextInput(),
                                label="Nachname",)

    email = forms.CharField(widget=forms.TextInput(),
                            label="Email",)

    date_of_birth = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        ),
        label="Geburtsdatum",
    )

    address = forms.CharField(
        label='Adresse',
        widget=forms.TextInput(attrs={'placeholder': 'Bohlweg 19'}),
    )

    city = forms.CharField(label="Stadt")
    zip_code = forms.CharField(label='PLZ')

    class Meta:
        model = Citizen
        fields = ('first_name', 'last_name', 'email', 'date_of_birth', 'address', 'city', 'zip_code')
