from django.contrib import admin
from .models import (
    Licenciatura, Docente, UnidadeCurricular,
    Tecnologia, Projeto, TFC,
    Competencia, Formacao, MakingOf
)


@admin.register(Licenciatura)
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ['sigla', 'nome', 'duracao_anos']
    search_fields = ['nome', 'sigla']


@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'url_pagina']
    search_fields = ['nome']


@admin.register(UnidadeCurricular)
class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ['nome', 'ano', 'semestre', 'ects', 'licenciatura']
    list_filter = ['ano', 'semestre', 'licenciatura']
    search_fields = ['nome']
    filter_horizontal = ('docentes',)


@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'categoria', 'nivel_interesse']
    list_filter = ['categoria', 'nivel_interesse']
    search_fields = ['nome']


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'ano', 'unidade_curricular']
    list_filter = ['ano', 'unidade_curricular']
    search_fields = ['nome']
    filter_horizontal = ('tecnologias',)


@admin.register(TFC)
class TFCAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'area', 'ano', 'interesse']
    list_filter = ['ano', 'interesse', 'area']
    search_fields = ['titulo', 'area']
    filter_horizontal = ('tecnologias',)


@admin.register(Competencia)
class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'nivel']
    list_filter = ['nivel']
    search_fields = ['nome']
    filter_horizontal = ('tecnologias', 'projetos')


@admin.register(Formacao)
class FormacaoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'instituicao', 'data_inicio', 'data_fim']
    list_filter = ['instituicao']
    search_fields = ['nome', 'instituicao']


@admin.register(MakingOf)
class MakingOfAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'entidade_relacionada', 'data']
    list_filter = ['entidade_relacionada']
    search_fields = ['titulo', 'entidade_relacionada']