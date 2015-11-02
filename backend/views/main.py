'''GENERAL VIEWS'''

# django imports
from django.http import JsonResponse

'''API version'''
def version(request):
    return JsonResponse({'version': '0.1.0'})