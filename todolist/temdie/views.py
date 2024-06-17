from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.http import JsonResponse
# Create your views here.

def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        
        if User.objects.filter(email=email).exists():
                messages.info(request, 'email already exist!')
                return render(request, 'register.html')
        else:
                user =  User.objects.create(name=name, email=email, password=password)
                user.save()
                messages.info(request, 'User created succesfully!')
                return render(request, 'login.html')
    else:

      return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.get(email=email, password=password)
        tags = TemdieTag.objects.filter(task__user=user)  
        tasks = user.temdietask_set.all()  

        context = {
            'user': user,
            'tags': tags,
            'tasks': tasks
        }

        return render(request, 'home.html', context)
        #messages.info(request, 'Invalid email or password')
            
    else:
        return render(request, 'login.html')

def updatestatus(request, task_id):
    task = TemdieTask.objects.get(id=task_id)
    task.completed = True
    task.save()
    return render(request, 'result.html')
 
