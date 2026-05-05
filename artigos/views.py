from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Artigo, Like, Comentario
from .forms import ArtigoForm, ComentarioForm

def artigos_view(request):
    artigos = Artigo.objects.all().order_by('-data_criacao')
    return render(request, 'artigos/artigos.html', {'artigos': artigos})

def artigo_view(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    comentarios = artigo.comentarios.all().order_by('data')
    form_comentario = ComentarioForm()
    return render(request, 'artigos/artigo.html', {
        'artigo': artigo,
        'comentarios': comentarios,
        'form_comentario': form_comentario,
        'total_likes': artigo.likes.count(),
    })

@login_required
def novo_artigo_view(request):
    if not request.user.groups.filter(name='autores').exists():
        return redirect('artigos')
    form = ArtigoForm(request.POST or None, request.FILES)
    if form.is_valid():
        artigo = form.save(commit=False)
        artigo.autor = request.user
        artigo.save()
        return redirect('artigos')
    return render(request, 'artigos/novo_artigo.html', {'form': form})

@login_required
def edita_artigo_view(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    if artigo.autor != request.user:
        return redirect('artigos')
    form = ArtigoForm(request.POST or None, request.FILES, instance=artigo)
    if form.is_valid():
        form.save()
        return redirect('artigo', artigo_id=artigo.id)
    return render(request, 'artigos/edita_artigo.html', {'form': form, 'artigo': artigo})

@login_required
def apaga_artigo_view(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    if artigo.autor == request.user:
        artigo.delete()
    return redirect('artigos')

def like_view(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    sessao = request.session.session_key
    if not sessao:
        request.session.create()
        sessao = request.session.session_key
    if not Like.objects.filter(artigo=artigo, sessao=sessao).exists():
        Like.objects.create(artigo=artigo, sessao=sessao)
    return redirect('artigo', artigo_id=artigo_id)

@login_required
def comentario_view(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    form = ComentarioForm(request.POST or None)
    if form.is_valid():
        comentario = form.save(commit=False)
        comentario.artigo = artigo
        comentario.autor = request.user
        comentario.save()
    return redirect('artigo', artigo_id=artigo_id)