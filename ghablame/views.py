from django.shortcuts import render
from .models import *
from .serializers import *
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.urls import reverse

def index(request):
    return render(request, 'ghablame/index.html')


def user_registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirmation = request.POST['confirmation']
        username_exists = Users.objects.values_list('username', flat=True)
        
        if confirmation != password:
            return render(request, 'authTest/register.html',{
                'message': ' !رمز عبور مطابقت ندارد, لطفا دوباره وارد کنید',
            })  
        elif username in username_exists is not None:
            return render(request, 'authTest/register.html',{
                'username_exists_message': 'کاربری با این نام کاربری از قبل وجود دارد',
            })  
        else:
            user = Users.objects.create_user(username,password)
            user.save()
            return HttpResponseRedirect(reverse('index'))
        
    else:
        return render(request, 'ghablame/index.html')


@csrf_exempt
def usersApi(request):
    users = Users.objects.all()

    if request.method == 'GET':
        serializer = UsersSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    if request.method == 'POST':
        data = JSONParser().parse(request)
        username = data['username']
        password = data['password']

        add_user = Users(
            username = username,
            password = password,
        )
        add_user.save()
        return HttpResponse(status=204) 
    
    else:
        return JsonResponse({"error": "GET or PUT request required."}, status=400)