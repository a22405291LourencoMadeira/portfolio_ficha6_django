from django.shortcuts import render, redirect
from .models import UnidadeCurricular, Projeto, Tecnologia, TFC, Competencia, Formacao, Licenciatura
from .forms import ProjetoForm, TecnologiaForm, CompetenciaForm, FormacaoForm

def index_view(request):
    licenciatura = Licenciatura.objects.first()
    return render(request, 'portfolio/index.html', {'licenciatura': licenciatura})

def ucs_view(request):
    ucs = UnidadeCurricular.objects.select_related('licenciatura').prefetch_related('docentes').all()
    return render(request, 'portfolio/ucs.html', {'ucs': ucs})

def tfcs_view(request):
    tfcs = TFC.objects.prefetch_related('tecnologias').all()
    return render(request, 'portfolio/tfcs.html', {'tfcs': tfcs})

def projetos_view(request):
    projetos = Projeto.objects.select_related('unidade_curricular').prefetch_related('tecnologias').all()
    return render(request, 'portfolio/projetos.html', {'projetos': projetos})

def novo_projeto_view(request):
    form = ProjetoForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('projetos')
    return render(request, 'portfolio/novo_projeto.html', {'form': form})

def edita_projeto_view(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    form = ProjetoForm(request.POST or None, request.FILES, instance=projeto)
    if form.is_valid():
        form.save()
        return redirect('projetos')
    return render(request, 'portfolio/edita_projeto.html', {'form': form, 'projeto': projeto})

def apaga_projeto_view(request, projeto_id):
    Projeto.objects.get(id=projeto_id).delete()
    return redirect('projetos')

def tecnologias_view(request):
    tecnologias = Tecnologia.objects.all()
    return render(request, 'portfolio/tecnologias.html', {'tecnologias': tecnologias})

def nova_tecnologia_view(request):
    form = TecnologiaForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('tecnologias')
    return render(request, 'portfolio/nova_tecnologia.html', {'form': form})

def edita_tecnologia_view(request, tec_id):
    tec = Tecnologia.objects.get(id=tec_id)
    form = TecnologiaForm(request.POST or None, request.FILES, instance=tec)
    if form.is_valid():
        form.save()
        return redirect('tecnologias')
    return render(request, 'portfolio/edita_tecnologia.html', {'form': form, 'tec': tec})

def apaga_tecnologia_view(request, tec_id):
    Tecnologia.objects.get(id=tec_id).delete()
    return redirect('tecnologias')

def competencias_view(request):
    competencias = Competencia.objects.prefetch_related('tecnologias', 'projetos').all()
    return render(request, 'portfolio/competencias.html', {'competencias': competencias})

def nova_competencia_view(request):
    form = CompetenciaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('competencias')
    return render(request, 'portfolio/nova_competencia.html', {'form': form})

def edita_competencia_view(request, comp_id):
    comp = Competencia.objects.get(id=comp_id)
    form = CompetenciaForm(request.POST or None, instance=comp)
    if form.is_valid():
        form.save()
        return redirect('competencias')
    return render(request, 'portfolio/edita_competencia.html', {'form': form, 'comp': comp})

def apaga_competencia_view(request, comp_id):
    Competencia.objects.get(id=comp_id).delete()
    return redirect('competencias')

def formacoes_view(request):
    formacoes = Formacao.objects.all().order_by('data_inicio')
    return render(request, 'portfolio/formacoes.html', {'formacoes': formacoes})

def nova_formacao_view(request):
    form = FormacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('formacoes')
    return render(request, 'portfolio/nova_formacao.html', {'form': form})

def edita_formacao_view(request, formacao_id):
    formacao = Formacao.objects.get(id=formacao_id)
    form = FormacaoForm(request.POST or None, instance=formacao)
    if form.is_valid():
        form.save()
        return redirect('formacoes')
    return render(request, 'portfolio/edita_formacao.html', {'form': form, 'formacao': formacao})

def apaga_formacao_view(request, formacao_id):
    Formacao.objects.get(id=formacao_id).delete()
    return redirect('formacoes')


def sobre_view(request):
    from .models import TipoTecnologia
    tipos = TipoTecnologia.objects.prefetch_related('tecnologias').all()
    return render(request, 'portfolio/sobre.html', {'tipos': tipos})

def makingof_view(request):
    from .models import MakingOf
    makingofs = MakingOf.objects.all().order_by('data')
    return render(request, 'portfolio/makingof.html', {'makingofs': makingofs})