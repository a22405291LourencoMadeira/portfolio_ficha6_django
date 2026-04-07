from django.db import models

class Licenciatura(models.Model):
    nome = models.CharField(max_length=200)
    sigla = models.CharField(max_length=20)
    descricao = models.TextField()
    url = models.URLField()
    duracao_anos = models.IntegerField()

    def __str__(self):
        return self.sigla