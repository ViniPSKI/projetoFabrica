import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from gerar_times.models import Aluno, Professor, Times, Aluno_com_time
from gerar_times.teamComposition import executar_algoritmo

@csrf_exempt
def gerar_time_api(request, tamanho):
    time = executar_algoritmo(int(tamanho))

    timeGerado = [{
        'Nome': Aluno.Nome,
        'id': Aluno.id,
        'Area_de_atuacao': Aluno.Area_de_atuacao,
        'Nivel_de_senioridade': Aluno.Nivel_de_senioridade,
        'Linguagem_Afinidade': Aluno.Linguagem_Afinidade,
        'RA': Aluno.RA,
        'Email': Aluno.Email,
        'Periodo': Aluno.Periodo
    } for Aluno in time]

    response_data = {'time': timeGerado}

    for i in range(tamanho):
        data = timeGerado
        dados = Aluno_com_time(Nome=data[i]['Nome'], 
        Area_de_atuacao=data[i]['Area_de_atuacao'], 
        Nivel_de_senioridade=data[i]['Nivel_de_senioridade'], 
        Linguagem_Afinidade=data[i]['Linguagem_Afinidade'], 
        RA=data[i]['RA'], Email=data[i]['Email'], 
        Periodo=data[i]['Periodo'], id=data[i]['id'])       
        dados.save()
        aluno = Aluno.objects.get(id = data[i]['id'])
        aluno.delete()

    ultimo_time = Times.objects.latest('id_time')
    id_times = ultimo_time.id_time
    id_atual = id_times +1
    print(id_atual)

    for y in range (tamanho):
        data1 = timeGerado
        time_info = Times(id_time=id_atual, id_aluno=data1[y]['id'])
        time_info.save()
    return JsonResponse(response_data, safe=False)
#@csrf_exempt
#def gerar_time_api(request, tamanho):
#    try:
#
#        if request.method == 'GET':
#
#            time = gerar_time(int(tamanho))
#
#            timeGerado = [{
#                'Nome': Aluno.Nome,
#                'RA': Aluno.RA,
#                'Area_de_atuacao': Aluno.Area_de_atuacao,
#                'Nivel_de_senioridade': Aluno.Nivel_de_senioridade,
#                'Linguagem_Afinidade': Aluno.Linguagem_Afinidade
#            } for Aluno in time]
#
#            response_data = {'time': timeGerado}
#
#            return JsonResponse(response_data, safe=False)
#        
#    except Exception as e:
#
#        return JsonResponse({'error': str(e)}, status=500)
    
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

            dados = Professor(Nome=data['nome'],
            Senha=data['senha'],
            Email=data['email'],
            Usuario=data['usuario'])

            if Professor.objects.filter(Email=dados.Email).exists():
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

            AlunosST = Aluno.objects.all()
            AlunosCT = Aluno_com_time.objects.all()

            lista_final = []

            listST = list(AlunosST.values())
            AlunosCT = list(AlunosCT.values())

            lista_final.append(listST)
            lista_final.append(AlunosCT)

            return JsonResponse(lista_final, safe=False)

    except Exception as e:
        
        return JsonResponse({'error': str(e)},status=500)


@csrf_exempt
def listar_Alunos_semTime(request):
    try:
        
        if request.method == 'GET':

            Alunos = Aluno.objects.all()

            #Transforma em uma lista de dicionários
            reponse_data = list(Alunos.values())
            
            #safe=False para corrigir o erro 'Object of type QuerySet is not JSON serializable'
            return JsonResponse(reponse_data, safe=False)

    except Exception as e:
        
        return JsonResponse({'error': str(e)},status=500)

@csrf_exempt
def listar_Times(request):
    try:
        
        if request.method == 'GET':
            times = Times.objects.all()
            reponse_data = list(times.values())
            return JsonResponse(reponse_data, safe=False)

    except Exception as e:
        return JsonResponse({'error': str(e)},status=500)


@csrf_exempt
def listar_membros_Times(request, idt):
    try:
        
        if request.method == 'GET':
            times = Times.objects.filter(id_time=idt)
            reponse_data = list(times.values())
            print(reponse_data[0]['id_aluno'])
            
            resultados_finais = []

            for X in range (5):
                dados_aluno = Aluno_com_time.objects.filter(id=reponse_data[X]['id_aluno'])

                resultado_final = list(dados_aluno.values())
                #resultado_final = {'id_aluno': id_aluno, 'dados_aluno': list(dados_aluno)}
                resultados_finais.append(resultado_final)

            return JsonResponse(resultados_finais, safe=False)

    except Exception as e:
        

        return JsonResponse({'error': str(e)},status=500)