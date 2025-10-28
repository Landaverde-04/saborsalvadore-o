from django.shortcuts import render

# Create your views here.

def lista_tipicos(request):
    """
    Vista para mostrar la lista de platos típicos salvadoreños
    """
    return render(request, 'lista-tipicos.html')
