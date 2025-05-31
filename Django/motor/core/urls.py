from django.urls import path
from .views import index, contato, sobre, veiculos, servicos, enviar_informacoes

urlpatterns = [
    path('',index),
    path('contato', contato),
    path('sobre', sobre),
    path('veiculos', veiculos),
    path('servicos', servicos),
    path('contato', contato),
    path('enviar_informacoes', enviar_informacoes),
]
