from django.shortcuts import render
from django.http import HttpResponse
from WEB.forms import *
from WEB.models import *
# Create your views here.

def Buscar_calzado(request):
    if request.method == "POST":
        nuevo_form = CalzadoForm(request.POST) #mostramos un formulario vacio
        if nuevo_form.is_valid():
            info = nuevo_form.cleaned_data
            nuevo_calzado=calzado(marca   = info["Marca"] ,
                                  tipo    =info["tipo"] ,
                                  color   =info["color"] ,
                                  talla   =info["talla"] ,
                                  genero  = info["genero"] 
                                  )
            nuevo_calzado.save()
            return render(request,"fullcarga.html" )
    else:
        nuevo_form=CalzadoForm()  
    return render(request,"calzado.html",{"mi_formu":nuevo_form})


def inicio(request):
    if request.method == "GET":
        marca_pedida = request.GET.get("marca", "")
        if marca_pedida:
            resultados_marca = calzado.objects.filter(marca__icontains=marca_pedida)
            return render(request, "inicio.html", {"zapatos": resultados_marca, "marca_pedida": marca_pedida})
    return render(request, "inicio.html", {"marca_pedida": ""})

def fullcarga(request):
    return render(request,"fullcarga.html" )

def Buscar_indumentaria(request):
    if request.method == "POST":
        nuevo_form = indumentariaForm(request.POST) #mostramos un formulario vacio
        if nuevo_form.is_valid():
            info = nuevo_form.cleaned_data
            nueva_indumentaria=indumentaria(marca=info["Marca"],
                                       tipo=info["tipo"],
                                       color=info["color"],
                                       talla=info["talla"],
                                       genero=info["genero"]
                                       )
            nueva_indumentaria.save()
            return render(request,"fullcarga.html" )
    else:
        nuevo_form=indumentariaForm()  
    return render(request,"indumentaria.html",{"mi_formu":nuevo_form})


def Buscar_accesorios(request):
    if request.method == "POST":
        nuevo_form = accesoriosForm(request.POST) #mostramos un formulario vacio
        if nuevo_form.is_valid():
            info = nuevo_form.cleaned_data
            nuevo_accesorios=accesorios(categoria=info["categoria"],
                                          marca=info["Marca"],
                                          deporte=info["deporte"]
                                          )
            nuevo_accesorios.save()
            return render(request,"fullcarga.html" )
    else:
        nuevo_form=accesoriosForm()  
    return render(request,"accesorios.html",{"mi_formu":nuevo_form})