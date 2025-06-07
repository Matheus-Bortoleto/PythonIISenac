from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('E-mail', max_length=100)
    def __str__(self):
        return f'{self.nome} {self.sobrenome}'