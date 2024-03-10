from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # uno = {'Primer_interes': 'Armar cubos rubik'}
    # dos = {'Segundo_interes': 'Música'}
    # tres = {'Tercer_interes': 'Los videojuegos de PC'}
    context = {
        'Primer_interes': 'Armar cubos rubik',
        'Segundo_interes': 'Música',
        'Tercer_interes': 'Los videojuegos de PC'
    }
    return render(request, "mi_app/index.html", context=context)

    #return HttpResponse("Mi primera chamba")

