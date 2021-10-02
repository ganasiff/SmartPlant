from django import forms
from django.db.models import fields
from .models import Settings

class SettingsForm(forms.ModelForm):
    class Meta:
        model = Settings
        fields = ['role','name','description']

    def clean(self):
        data  = self.cleaned_data
        name = data.get("name")
        qs = Settings.objects.filter(name__icontains = name)
        if qs.exists():
            self.add_error("name",f"{name} ya esta ocupado.")

        return data


class Settings_form_old(forms.Form):
    role = forms.CharField()
    description = forms.CharField()