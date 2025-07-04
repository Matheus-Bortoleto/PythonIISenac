from django.db import models
from datetime import datetime
from funcionario.models import Funcionario

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('E-mail', max_length=100)
    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
    
class Prato(models.Model):
    nome_prato = models.CharField(max_length = 100)
    ingredientes = models.TextField()
    modo_preparo = models.CharField(max_length = 100)
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length = 100)
    categoria = models.CharField(max_length = 100)
    date_prato= models.DateTimeField(default = datetime.now, blank=True)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    publicado = models.BooleanField(default=False)
    foto_prato = models.ImageField(upload_to='pratos/%y/%m/%d', blank=True)

    def __str__(self):
        return self.nome_prato