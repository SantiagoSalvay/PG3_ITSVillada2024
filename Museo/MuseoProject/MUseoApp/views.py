from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views import View
from django.views.generic import TemplateView
import requests
from typing import Any
def primera_vista(request: HttpRequest):
    if request.method == 'GET':
        return HttpResponse("<h1>Hola, esta es mi primera vista!</h1> Y solo permito GET.")

class PrimeraVista(View):
    def get(self, request, *args, **kwargs):
        return render(request, "primeraClase.html")

class PrimerTemplateView(TemplateView):
    template_name = "primeraClase.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['mensaje'] = "Hola chicos, como va?"
        res = requests.get("https://www.cultura.gob.ar/api/v2.0/museos/")
        res_json = res.json()
        museos_res = res_json.get('results')
        print(f'NICO: {museos_res}')
        context['museos'] = museos_res
        return context

