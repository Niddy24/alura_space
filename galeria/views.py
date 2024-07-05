from django.shortcuts import render


def index(request):
    dados = {
    1: {'nome': 'Nebulosa de Carina',
        'legenda': 'webbtelescope.org / NASA / james Webb' 
        },
    2: {
        'nome': 'Galaxia NGC 1079',
        'legenda': 'NASA.org / NASA : Hunbble'
        },
            }
    return render(request, 'galeria/index.html' , {'cards': dados})

def imagem(request):
    return render(request, 'galeria/imagem.html')
