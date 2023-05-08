from django.shortcuts import render
from .models import *
from .serializers import *
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

def index(request):
    return render(request, 'ghablame/index.html')


@csrf_exempt
def usersApi(request):
    users = Users.objects.all()
    if request.method == 'GET':
        serializer = UsersSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({"error": "GET or PUT request required."}, status=400)