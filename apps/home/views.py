# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import os
from django import template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.conf import settings
import pandas as pd
import plotly.express as px
from django.shortcuts import render

def pages(request):
    context = {}
    # Verifica que la URL termina en .html
    load_template = request.path.split('/')[-1]

    if not load_template.endswith('.html'):
        return HttpResponse("Invalid request", status=400)

    if load_template == 'admin':
        return HttpResponseRedirect(reverse('admin:index'))

    context['segment'] = load_template

    try:
        # Intenta cargar la plantilla
        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:
        # Manejo del error si la plantilla no existe
        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except Exception as e:
        # Manejo de otros errores
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

def index(request):
    return render(request, 'home/index.html') 



def csv_plot_view(request):
    # Construir la ruta al archivo CSV dentro de static
    csv_file_path = os.path.join(settings.BASE_DIR, 'static', 'temperatura.csv')

    
    # Leer el archivo CSV   
    data = pd.read_csv(csv_file_path, delimiter=";")


    # Crear el gráfico (ejemplo: gráfico de dispersión)
    fig = px.line(data, x='Año', y='Periodo', title='Gráfico de Temperatura')

    # Convertir el gráfico a HTML
    graph_html = fig.to_html(full_html=False)

    # Renderizar el gráfico en la plantilla
    return render(request, 'home/index.html', {'graph': graph_html})

def csv_plot_view_evol_CO2(request):
    # Construir la ruta al archivo CSV dentro de static
    csv_file_path = os.path.join(settings.BASE_DIR, 'static', 'temperatura.csv')

    
    # Leer el archivo CSV   
    data = pd.read_csv(csv_file_path, delimiter=";")


    # Crear el gráfico (ejemplo: gráfico de dispersión)
    fig = px.line(data, x='Año', y='Periodo', title='Gráfico de Temperatura')

    # Convertir el gráfico a HTML
    graph_html = fig.to_html(full_html=False)

    # Renderizar el gráfico en la plantilla
    return render(request, 'home/index.html', {'graph_evol_co2': graph_html})