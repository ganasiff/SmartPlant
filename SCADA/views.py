from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import SettingsForm
from .models import Settings

from datetime import datetime, date
# Create your views here.
from django.http import HttpResponse
import random

def indice(request):

    random_list =[]
    for i in range(0,7):
        random_list.append(random.randint(10000,25000))
    if request.user.is_authenticated:    
        fecha_actual= date.today()
        tiempo_actual= datetime.now()
        list_settings = Settings.objects.all()[:10]
        diccionario = { 'System_time': tiempo_actual.strftime("%H:%M:%S"),
                        'System_date': fecha_actual.strftime("%B %d, %Y"),
                        "list" : list_settings,
                        "dj_chart": random_list,
                        }
    else:
        diccionario = {}

    return render(request,"Scada/index.html", context=diccionario)

@login_required
def settings_scada(request,id=None):
 
    list_settings = Settings.objects.all()[:10]

    form = SettingsForm(request.POST or None)
    #print(Settings.Meta.model.role())
    context = {
        "form": form,
        "list" : list_settings,
    }   
    if form.is_valid():
        obj_settings = form.save()
        #print(dir(obj_settings))
        context['role','name','description','status'] = obj_settings #desde DB
        print(obj_settings.role)
        print(obj_settings.description)

    print(context)

    return render(request,"Scada/settings.html", context=context)
#Class based view
class Settings_edit(UpdateView):
    model = Settings
    form_class = SettingsForm
    template_name = 'Scada/settings_edit.html'
    #fields = ['role','name','description','status']
    
class Settings_delete(DeleteView):
    model = Settings   
    template_name = 'Scada/settings_delete.html'
    success_url = reverse_lazy('settings')
    

def settings_scada_search(request):
    query_dict = request.GET
    query = query_dict.get("search")
    obj_settings= None
    if query is not None:
        obj_settings =Settings.objects.get(id=query)

    context = {
        "object" : obj_settings
    }
    return render(request, "Scada/search.html", context=context)