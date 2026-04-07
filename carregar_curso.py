import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from portfolio.models import Licenciatura, UnidadeCurricular

# Lê o ficheiro JSON
with open('files/ULHT260-PT.json', encoding='utf-8') as f:
    dados = json.load(f)

# Atualiza a descrição da Licenciatura com as razões
lic = Licenciatura.objects.get(sigla='LEI')
razoes = '\n'.join([r['reason'] for r in dados['reasons']])
lic.descricao = razoes
lic.save()
print("Licenciatura atualizada!")

# Apaga UCs existentes para evitar duplicados
UnidadeCurricular.objects.all().delete()

# Carrega as UCs
for uc in dados['courseFlatPlan']:
    UnidadeCurricular.objects.create(
        nome=uc['curricularUnitName'],
        ano=uc['curricularYear'],
        semestre=1 if uc['semesterCode'] == 'S' else 2,
        descricao='',
        ects=uc['ects'],
        licenciatura=lic,
    )

print(f'{UnidadeCurricular.objects.count()} UCs carregadas com sucesso!')