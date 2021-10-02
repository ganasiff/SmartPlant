from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import SettingsForm
from .models import Settings

from datetime import datetime, date
# Create your views here.
from django.http import HttpResponse


def indice(request):
    if request.user.is_authenticated:    
        fecha_actual= date.today()
        tiempo_actual= datetime.now()
        diccionario = { 'System_time': tiempo_actual.strftime("%H:%M:%S"),
                        'System_date': fecha_actual.strftime("%B %d, %Y"),
                        }
    else:
        diccionario = {}

    return render(request,"Scada/index.html", context=diccionario)
@login_required
def settings_scada(request,id=None):
 
    form = SettingsForm(request.POST or None)
    #print(Settings.Meta.model.role())
    context = {
        "form": form
    }   
    if form.is_valid():
        obj_settings = form.save()
        #print(dir(obj_settings))
        context['role','name','description'] = obj_settings #desde DB
    else:
        obj_settings = Settings.objects.get(id=id)
        obj_settings.role = "N/A"
        obj_settings.description = "N/A"
        print(obj_settings.role)
        print(obj_settings.description)
        #obj_settings[0]= "1"
        #obj_settings[1] = "N/A"
        #obj_settings[2] = "N/A"
        context['role','description'] = obj_settings #sin info relevante
    print(context)
    return render(request,"Scada/settings.html", context=context)

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