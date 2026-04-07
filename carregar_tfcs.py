import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from portfolio.models import TFC

# Apaga TFCs existentes para evitar duplicados
TFC.objects.all().delete()

# Lê o ficheiro JSON
with open('data/tfcs_2024_2025.json', encoding='utf-8') as f:
    tfcs = json.load(f)

# Carrega cada TFC na base de dados
for t in tfcs:
    TFC.objects.create(
        titulo=t['titulo'],
        autor=t['autor'],
        orientador=t['orientador'],
        curso=t['curso'],
        ano=int(t['ano']),
        interesse=t['rating'] >= 4,  # marca como interesse se rating >= 4
    )

print(f'{TFC.objects.count()} TFCs carregados com sucesso!')