from django.http import HttpResponse
from django.shortcuts import render
from django.template.exceptions import TemplateDoesNotExist, TemplateSyntaxError

def lista_tipicos(request):
    try:
        return render(request, "lista-tipicos.html")
    except TemplateDoesNotExist as e:
        return HttpResponse(f"NO ENCONTRE TEMPLATE: {e}", status=500)
    except TemplateSyntaxError as e:
        return HttpResponse(f"ERROR DE SINTAXIS EN TEMPLATE: {e}", status=500)
    except Exception as e:
        return HttpResponse(f"OTRO ERROR: {e}", status=500)

