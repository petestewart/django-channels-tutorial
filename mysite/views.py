# from rest_framework.viewsets import ViewSet
from django.http import JsonResponse

def hello(request):
        """Return a dummy list"""

        answer = {"hello": "world"}

        return JsonResponse(answer)