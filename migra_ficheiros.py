import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from django.core.files import File
from portfolio.models import Docente, UnidadeCurricular, Tecnologia, Projeto, MakingOf

print("A migrar Docentes...")
for obj in Docente.objects.all():
    if obj.foto and obj.foto.name:
        local_path = os.path.join('media', obj.foto.name)
        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.foto.save(os.path.basename(local_path), File(f), save=True)
            print(f"Migrado: {obj}")

print("A migrar Unidades Curriculares...")
for obj in UnidadeCurricular.objects.all():
    if obj.imagem and obj.imagem.name:
        local_path = os.path.join('media', obj.imagem.name)
        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.imagem.save(os.path.basename(local_path), File(f), save=True)
            print(f"Migrado: {obj}")

print("A migrar Tecnologias...")
for obj in Tecnologia.objects.all():
    if obj.logo and obj.logo.name:
        local_path = os.path.join('media', obj.logo.name)
        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.logo.save(os.path.basename(local_path), File(f), save=True)
            print(f"Migrado: {obj}")

print("A migrar Projetos...")
for obj in Projeto.objects.all():
    if obj.imagem and obj.imagem.name:
        local_path = os.path.join('media', obj.imagem.name)
        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.imagem.save(os.path.basename(local_path), File(f), save=True)
            print(f"Migrado: {obj}")

print("A migrar MakingOf...")
for obj in MakingOf.objects.all():
    if obj.fotografia and obj.fotografia.name:
        local_path = os.path.join('media', obj.fotografia.name)
        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.fotografia.save(os.path.basename(local_path), File(f), save=True)
            print(f"Migrado: {obj}")

print("Migração concluída!")