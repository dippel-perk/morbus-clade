from django import forms
from .models import Citizen, ContactPerson
from phonenumber_field.formfields import PhoneNumberField


class CitizenForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(),
                                 label="Vorname")
    last_name = forms.CharField(widget=forms.TextInput(),
                                label="Nachname", )

    email = forms.CharField(widget=forms.TextInput(),
                            label="Email",
                            help_text="Über diese Adresse erhalten Sie alle Informationen zum Testergebnis")

    telephone = PhoneNumberField(label="Telefonnummer", help_text="Für eventuelle Rückfragen vom Gesundheitsamt")

    date_of_birth = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        ),
        label="Geburtsdatum",

    )

    address = forms.CharField(
        label='Adresse',
        widget=forms.TextInput(attrs={}),
        help_text="Strassenname und Hausnummer"
    )

    city = forms.CharField(label="Stadt")
    zip_code = forms.CharField(label='PLZ')

    class Meta:
        model = Citizen
        fields = ('first_name', 'last_name', 'email', 'telephone', 'date_of_birth', 'address', 'city', 'zip_code')


class ContactPersonForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(),
                                 label="Vorname")
    last_name = forms.CharField(widget=forms.TextInput(),
                                label="Nachname", )

    email = forms.CharField(widget=forms.TextInput(),
                            label="Email",
                            help_text="")

    telephone = PhoneNumberField(label="Telefonnummer", help_text="")

    last_contact = forms.DateTimeField(label="Letzter Kontakt", input_formats=['%d.%m.%Y %H:%M'],
                                       widget=forms.TextInput(
                                           attrs={'id': 'lastContactInput', 'autocomplete': 'off'}
                                       ), help_text="Wann war ihr letzter physischer Kontakt mit dieser Person?")
    description = forms.CharField(max_length=300,
                                  widget=forms.Textarea,
                                  label="Beschreibung",
                                  help_text="Wo haben Sie die Kontaktperson zuletzt getroffen. Beschreiben Sie die Situation")

    class Meta:
        model = ContactPerson
        fields = ('first_name', 'last_name', 'email', 'telephone', 'last_contact', 'description')
