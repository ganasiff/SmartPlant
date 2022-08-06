from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect, render
from django.views.generic import ListView,CreateView ,UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import SettingsForm, SettingsFormEdit
from .models import Settings
from datetime import datetime, date
from django.http import HttpResponse, response
import random

#DjangoREST
from rest_framework.views import APIView
from rest_framework.response import Response


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
#@login_required
@method_decorator(login_required, name='dispatch')
class Settings_Create(CreateView):
    model = Settings
    form_class= SettingsForm
    template_name='Scada/settings_create.html'
    success_url= reverse_lazy('settings')

@method_decorator(login_required, name='dispatch')
class Settings_list(ListView):
    model=Settings
    template_name="Scada/settings_list.html"


class Settings_edit(UpdateView):
    model = Settings
    form_class = SettingsFormEdit
    template_name = 'Scada/settings_edit.html'
    #fields = ['role','name','description','status']
    

class Settings_delete(DeleteView):
    model = Settings   
    template_name = 'Scada/settings_delete.html'
    success_url = reverse_lazy('settings')
    

def settings_scada_search(request):
    query_dict = request.GET
    try:
        query = query_dict.get("search")
    except:
        query=None
    obj_settings= None
    if query is not None:
        obj_settings =Settings.objects.get(id=query)

    context = {
        "object_list" : obj_settings
    }
    return render(request, "Scada/search.html", context=context)

class HelloWorld(APIView):
    def get(self,request):
        return Response('Hola Juan Carrlos...')