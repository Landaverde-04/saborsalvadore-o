from django.shortcuts import render

# Create your views here.

def lista_tipicos(request):
    return render(request, 'ModuloTipicos/lista-tipicos.html')
