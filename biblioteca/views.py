from django.http import JsonResponse

def biblioteca(request):
    if request.method == 'GET':
        biblioteca = {'id':1, 'nome':'Rhama'}
        return JsonResponse(aluno)
