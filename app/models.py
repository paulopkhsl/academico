from django.db import models


class Cidade(models.Model):
    nome = models.CharField(max_length = 100)
    uf = models.CharField(max_length = 100)
    
class Ocupacao(models.Model):
    nome = models.CharField(max_length = 100)

class Pessoa(models.Model):
    nome = models.CharField(max_length=100 )
    pai = models.CharField(max_length=100 )
    mae = models.CharField(max_length=100 )
    cpf = models.CharField(max_length=14)
    data_nasc = models.CharField(max_length=100 )
    email = models.CharField(max_length=100 )
    cidade = models.ForeignKey(Cidade, on_delete = models.CASCADE)
    ocupacao = models.ForeignKey(Ocupacao, on_delete = models.CASCADE)
    

class Instituicao(models.Model):
    nome = models.CharField(max_length = 100)
    site = models.CharField(max_length = 100)
    telefone = models.CharField(max_length = 100)
    cidade = models.ForeignKey(Cidade, on_delete = models.CASCADE)
    
    
class Areas(models.Model):

    nome = models.CharField(max_length = 100)
    