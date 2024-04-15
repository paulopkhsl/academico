
 
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('area/',AreaView.as_view(),name='area'),
    path('',TemplateView.as_view(),name='index'),
    path('ocupacao/', OcupacaoView.as_view(), name='ocupacao'),
    path('cidade/', CidadeView.as_view(),name='cidade'),
    path('pessoa/', PessoaView.as_view(),name='pessoa'),
    path('instituicao/', InstituicaoView.as_view(), name='instituicao'),
    path('curso/', CursoView.as_view(),name='curso'),
    path('disciplina/', DisciplinaView.as_view(),name='disciplina'),
    path('periodo/', PeriodoView.as_view(),name='periodo'),
    path('matricula/', MatriculaView.as_view(),name='matricula'),
    path('avaliacao/', AvaliacaoView.as_view(),name='avaliacao'),
    path('frequencia/', FrequenciaView.as_view(),name='frequencia'),
    path('turma/', TurmaView.as_view(),name='turma'),
    path('ocorrencia/', OcorrenciaView.as_view(),name='ocorrencia'),
    path('disciplina_curso/', Disciplina_cursoView.as_view(),name='disciplina_curso'),
    path('tipos_avaliacao/', Tipos_avaliacaoView.as_view(),name='tipos_avaliacao'),
]
