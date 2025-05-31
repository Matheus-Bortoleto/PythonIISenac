from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html') 

def contato(request):
    return render(request, 'contato.html') 

def servicos(request):
    return render(request, 'servicos.html') 

def sobre(request):
    return render(request, 'sobre.html') 

def veiculos(request):
    return render(request, 'veiculos.html') 

def enviar_informacoes(request):
    return render(request, 'enviar_informacoes.html') 

def contato(request):
    context = {
        'nome':'MotorWeb',
        'fone':'17 7070-6070',
        'email':'contato@motorweb.com' 
    }
    return render(request, 'contato.html', context)