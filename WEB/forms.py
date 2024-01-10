from django import forms

class CalzadoForm(forms.Form):
    Marca=forms.CharField()
    tipo    = forms.CharField()
    color   = forms.CharField()
    talla   = forms.IntegerField()
    genero  = forms.CharField()


class indumentariaForm(forms.Form):
    Marca   = forms.CharField()
    tipo    = forms.CharField()
    color   = forms.CharField()
    talla   = forms.IntegerField()
    genero  = forms.CharField()

class accesoriosForm(forms.Form):
    Marca   = forms.CharField()
    categoria   = forms.CharField()
    deporte   = forms.CharField()
    