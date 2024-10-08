from django.http import HttpResponse, JsonResponse
from .models import Proyecto
from .forms import ProyectoForm
from django.shortcuts import render, redirect

# Create your views here.
def blockk (req, parametro):

    result = list(Proyecto.objects.values())

    print("Se imprimop red:" ,)

    return JsonResponse({
        "nada": "Si",
        "parametro": parametro,
        "result": result
    }, safe=False)

# Create your views here.
def index (req):

    if req.method == 'POST':
        form = ProyectoForm(req.POST)
        if form.is_valid():
            form.save()
            print("guardo informacion")
            return redirect("/")
    else:
        form = ProyectoForm()  # Si es GET, crea un formulario vacío

    backend = "Este texto viene desde el backend"

    return render(req, "index/index.html", {
        "backend": backend,
        'form': form
    })


    