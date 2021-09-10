from django.shortcuts import render

from datetime import datetime, date
# Create your views here.
from django.http import HttpResponse


def indice(request):
    fecha_actual= date.today()
    tiempo_actual= datetime.now()
    diccionario = { 'System_time': tiempo_actual.strftime("%H:%M:%S"),
                    'System_date': fecha_actual.strftime("%B %d, %Y"),
                    }
    return render(request,"Scada/index.html", context=diccionario)