from django import forms
from django.db.models import fields
#from django.forms.forms import Form
from .models import Settings


class SettingsForm(forms.ModelForm):
    class Meta:
        model = Settings
        fields = ['role','name','description','status']#de models.py

        widgets = {
            'role' : forms.Select(attrs = {'class':'form-control'}),
            'name' : forms.TextInput(attrs = {'class':'form-control', "placeholder":"Nombre de Nodo"}),
            'description' : forms.TextInput(attrs = {'class':'form-control',"placeholder":"Breve Descripcion"}),
            'status' : forms.Select(attrs = {'class':'form-control'}),
            #'role' : forms.TextInput(attrs = {'class':'form-control', 'type':'text','name':'role','id':'role'}),
            #'name' : forms.TextInput(attrs = {'class':'form-control', 'type':'text','name':'name','id':'name'}),
            #'description' : forms.TextInput(attrs = {'class':'form-control', 'type':'text','name':'description','id':'description'})
            #put class="form-control" type="text" name="username" id="username
        }

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