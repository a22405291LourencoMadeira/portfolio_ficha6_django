from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='portfolio_index'),
    path('ucs/', views.ucs_view, name='ucs'),
    path('projetos/', views.projetos_view, name='projetos'),
    path('tecnologias/', views.tecnologias_view, name='tecnologias'),
    path('tfcs/', views.tfcs_view, name='tfcs'),
    path('competencias/', views.competencias_view, name='competencias'),
    path('formacoes/', views.formacoes_view, name='formacoes'),
    path('projetos/novo/', views.novo_projeto_view, name='novo_projeto'),
path('projetos/<int:projeto_id>/edita/', views.edita_projeto_view, name='edita_projeto'),
path('projetos/<int:projeto_id>/apaga/', views.apaga_projeto_view, name='apaga_projeto'),
path('tecnologias/nova/', views.nova_tecnologia_view, name='nova_tecnologia'),
path('tecnologias/<int:tec_id>/edita/', views.edita_tecnologia_view, name='edita_tecnologia'),
path('tecnologias/<int:tec_id>/apaga/', views.apaga_tecnologia_view, name='apaga_tecnologia'),
]