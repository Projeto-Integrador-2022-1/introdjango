from django.shortcuts import render

# Create your views here.
def home(request):
    contexto = {
        'nome': 'Felipe',
        'notas': [0,2,-16, 8.5, 3.2],
    }


    return render(request, 'aula1808/index.html', context=contexto)
