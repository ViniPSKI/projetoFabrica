from django.urls import path
from gerar_times import views

urlpatterns = [
    path('gerar_time/<int:tamanho>/', views.gerar_time_api, name='gerar_time_api'),
    path('salvar_dados_aluno/', views.salvar_dados_Aluno, name='salvar_dados_aluno'),
    path('salvar_dados_professor/', views.salvar_dados_Professor, name='salvar_dados_professor'),
    path('listar_alunos/', views.listar_Alunos, name='listar_alunos'),
    path('listar_alunos_semTime/', views.listar_Alunos_semTime, name='listar_alunos_semtime'),
    path('listar_times/', views.listar_Times, name='listar_times'),
    path('listar_membros_time/<int:idt>', views.listar_membros_Times, name='listar_membros_times'),
]
