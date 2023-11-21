import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from gerar_times.models import Aluno, Professor
from gerar_times.teamComposition import executar_algoritmo

@csrf_exempt
def gerar_time_api(request, tamanho):
    time = executar_algoritmo(int(tamanho))

    timeGerado = [{
        'Nome': Aluno.Nome,
        'RA': Aluno.RA,
        'Area_de_atuacao': Aluno.Area_de_atuacao,
        'Nivel_de_senioridade': Aluno.Nivel_de_senioridade,
        'Linguagem_Afinidade': Aluno.Linguagem_Afinidade
    } for Aluno in time]

    response_data = {'time': timeGerado}

    return JsonResponse(response_data, safe=False)

#@csrf_exempt
#def gerar_time_api(request, tamanho):
    try:

        if request.method == 'GET':

            time = gerar_time(int(tamanho))

            timeGerado = [{
                'Nome': Aluno.Nome,
                'RA': Aluno.RA,
                'Area_de_atuacao': Aluno.Area_de_atuacao,
                'Nivel_de_senioridade': Aluno.Nivel_de_senioridade,
                'Linguagem_Afinidade': Aluno.Linguagem_Afinidade
            } for Aluno in time]

            response_data = {'time': timeGerado}

            return JsonResponse(response_data, safe=False)
        
    except Exception as e:

        return JsonResponse({'error': str(e)}, status=500)
    
@csrf_exempt
def salvar_dados_Aluno(request):

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
def salvar_dados_Professor(request):

    try:
        if request.method == 'POST':

            data = json.loads(request.body)

            dados = Professor(nome=data['nome'],
            senha=data['senha'],
            email=data['email'],
            usuario=data['usuario'])

            if Professor.objects.filter(email=dados.email).exists():
                return JsonResponse({'error': 'Email já cadastrado'}, status=400)

            dados.save()

            return JsonResponse({'message': 'Dados salvos com sucesso'})
        
        else:

            return JsonResponse({'error': 'Método não permitido'}, status=405)
        
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
@csrf_exempt
def listar_Alunos(request):
    try:
        
        if request.method == 'GET':

            Alunos = Aluno.objects.all()

            #Transforma em uma lista de dicionários
            reponse_data = list(Alunos.values())
            
            #safe=False para corrigir o erro 'Object of type QuerySet is not JSON serializable'
            return JsonResponse(reponse_data, safe=False)

    except Exception as e:
        
        return JsonResponse({'error': str(e)},status=500)

