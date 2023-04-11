from django.http import JsonResponse

def reverse_string(request):
    if request.method == 'GET':
        string = request.GET.get('string')
        reversed_string = string[::-1]
        data = {'reversed_string': reversed_string}
        return JsonResponse(data)
    else:
        data = {'error': 'Invalid request method'}
        return JsonResponse(data, status=405)

# Create your views here.
