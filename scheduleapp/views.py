from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse


def index(request):
    jornadas = ['mañana', 'tarde', 'noche']
    dias = ['Lunes','Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
    horario_mañana = ['8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00']
    horario_tarde = ['13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00']
    horario_noche = ['19:30', '20:00', '20:30', '21:00', '21:30', '22:00', '22:30', '23:00', '23:30', '24:00']
    context = {
        'jornadas': jornadas,
        'dias': dias,
        'horario_mañana': horario_mañana,
        'horario_tarde': horario_tarde,
        'horario_noche': horario_noche,
    }
    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))


def recibir_disponibilidad_horaria(request, dia, jornada, hora):
    print(dia)
    print(jornada)
    print(hora)
    return HttpResponseRedirect(reverse('index'))




