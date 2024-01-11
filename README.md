# Pre-entrega-3

Explicacion:

En el Proyecto existen 3 models cada columna tiene su significado esto lo explico para el momento que necesiten ingresar los datos:

calzado
    marca= marca de las zapatillas
    tipo= tipos (running, casual, urban)
    color
    talla
    genero= hombre mujer, niño etc


indumentaria
    marca= marca de las ropa
    tipo= musculosa, fit, de fut etc
    color
    talla 
    genero=  hombre mujer, niño etc

accesorios
    categoria = gym, atletimos etc
    marca
    deporte= fut, baloncesto etc 
	
	
	
Tiene 5 vistas:
Para ingresar datos estan:
accesorios.html,calzado.html,fullcarga.html,indumentaria.html
las clases son:

def Buscar_calzado(request)

def fullcarga(request)

def Buscar_indumentaria(request)


Para buscar Datos:

inicio.html

las clases son:
def inicio(request)

Tengo una vista que cuando termina de ingresar un datos muestra full carga:

fullcarga.html

Una html padre que lo demas toma como herencia:

padre.html
