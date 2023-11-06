import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from gerar_times.models import Aluno, Professor
from gerar_times.teamComposition import gerar_time

@csrf_exempt
def gerar_time_api(request, tamanho):
    try:

        if request.method == 'GET':

            time = gerar_time(int(tamanho))

            timeGerado = [{
                'Nome': aluno.Nome,
                'RA': aluno.RA,
                'Area_de_atuacao': aluno.Area_de_atuacao,
                'Nivel_de_senioridade': aluno.Nivel_de_senioridade,
                'Linguagem_Afinidade': aluno.Linguagem_Afinidade
            } for aluno in time]

            response_data = {'time': timeGerado}

            return JsonResponse(response_data, safe=False)
        
    except Exception as e:

        return JsonResponse({'error': str(e)}, status=500)
    
@csrf_exempt
def salvar_dados_aluno(request):

    try:

        if request.method == 'POST':

            data = json.loads(request.body)

            dados = Aluno(Nome=data['nome'], 
            Area_de_atuacao=data['papel'], 
            Nivel_de_senioridade=data['nivel'], 
            Linguagem_Afinidade=data['linguagem'], 
            RA=data['ra'], Email=data['email'], 
            Periodo=data['periodo'])

            if Aluno.objects.filter(RA=dados.RA).exists():
                return JsonResponse({'error':'RA já cadastrado'},status=400)

            dados.save()
            return JsonResponse({'message': 'Dados salvos com sucesso'})
         
        else:

            return JsonResponse({'error': 'Método não permitido'}, status=405)
        
    except Exception as e:

        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt   
def salvar_dados_professor(request):

    try:

        if request.method == 'POST':

            data = json.loads(request.body)

            dados = Professor(Nome=data['nome'], 
            Senha=data['senha'], 
            Email=data['email'])

            if Professor.objects.filter(Email=dados.Email).exists():
                return JsonResponse({'error':'Email já cadastrado'},status=400)

            dados.save()

            return JsonResponse({'message': 'Dados salvos com sucesso'})
        
        else:

            return JsonResponse({'error': 'Método não permitido'}, status=405)
        
    except Exception as e:

        return JsonResponse({'error': str(e)}, status=500)
    
@csrf_exempt
def listar_alunos(request):
    try:
        
        if request.method == 'GET':

            alunos = Aluno.objects.all()

            #Transforma em uma lista de dicionários
            reponse_data = list(alunos.values())
            
            #safe=False para corrigir o erro 'Object of type QuerySet is not JSON serializable'
            return JsonResponse(reponse_data, safe=False)

    except Exception as e:
        
        return JsonResponse({'error': str(e)},status=500)