from django.db import models

class Licenciatura(models.Model):
    nome = models.CharField(max_length=200)
    sigla = models.CharField(max_length=20)
    descricao = models.TextField()
    url = models.URLField()
    duracao_anos = models.IntegerField()

    def __str__(self):
        return self.sigla


class Docente(models.Model):
    nome = models.CharField(max_length=200)
    url_pagina = models.URLField()
    foto = models.ImageField(upload_to='docentes/', blank=True, null=True)

    def __str__(self):
        return self.nome


class UnidadeCurricular(models.Model):
    nome = models.CharField(max_length=200)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='ucs/', blank=True, null=True)
    ects = models.IntegerField()
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE, related_name='ucs')
    docentes = models.ManyToManyField(Docente, related_name='ucs', blank=True)

    def __str__(self):
        return self.nome

class TipoTecnologia(models.Model):
    TIPOS = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('base_dados', 'Base de Dados'),
        ('storage', 'Storage'),
        ('outro', 'Outro'),
    ]
    nome = models.CharField(max_length=50, choices=TIPOS)

    def __str__(self):
        return self.nome        


class Tecnologia(models.Model):
    CATEGORIAS = [
        ('linguagem', 'Linguagem'),
        ('framework', 'Framework'),
        ('base_dados', 'Base de Dados'),
        ('ferramenta', 'Ferramenta'),
        ('outro', 'Outro'),
    ]
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    logo = models.ImageField(upload_to='tecnologias/', blank=True, null=True)
    url_website = models.URLField()
    nivel_interesse = models.IntegerField()  # 1 a 5
    tipo = models.ForeignKey(TipoTecnologia, on_delete=models.SET_NULL, null=True, blank=True, related_name='tecnologias')

    def __str__(self):
        return self.nome


class Projeto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    conceitos = models.TextField()
    imagem = models.ImageField(upload_to='projetos/', blank=True, null=True)
    video_demo = models.URLField(blank=True, null=True)
    url_github = models.URLField()
    ano = models.IntegerField()
    unidade_curricular = models.ForeignKey(UnidadeCurricular, on_delete=models.CASCADE, related_name='projetos')
    tecnologias = models.ManyToManyField(Tecnologia, related_name='projetos', blank=True)

    def __str__(self):
        return self.nome


class TFC(models.Model):
    titulo = models.TextField()
    autor = models.TextField()
    orientador = models.TextField()
    curso = models.TextField()
    ano = models.IntegerField()
    interesse = models.BooleanField(default=False)
    url = models.URLField(blank=True, null=True)
    tecnologias = models.ManyToManyField(Tecnologia, related_name='tfcs', blank=True)

    def __str__(self):
        return self.titulo


class Competencia(models.Model):
    NIVEIS = [
        ('basico', 'Básico'),
        ('intermedio', 'Intermédio'),
        ('avancado', 'Avançado'),
    ]
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    nivel = models.CharField(max_length=20, choices=NIVEIS)
    tecnologias = models.ManyToManyField(Tecnologia, related_name='competencias', blank=True)
    projetos = models.ManyToManyField(Projeto, related_name='competencias', blank=True)

    def __str__(self):
        return self.nome


class Formacao(models.Model):
    nome = models.CharField(max_length=200)
    instituicao = models.CharField(max_length=200)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_fim = models.DateField(blank=True, null=True)
    certificado_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nome


class MakingOf(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    decisoes = models.TextField()
    erros_correcoes = models.TextField()
    uso_ia = models.TextField(blank=True)
    fotografia = models.ImageField(upload_to='makingof/', blank=True, null=True)
    data = models.DateField()
    entidade_relacionada = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo