from django.contrib import admin
from .models import Licenciatura

@admin.register(Licenciatura)
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ['sigla', 'nome', 'duracao_anos']
    search_fields = ['nome', 'sigla']