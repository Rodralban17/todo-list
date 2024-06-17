from django.shortcuts import render, get_object_or_404
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
    return render(request, 'result.html', {'result': "Task status updated to complete"})

def addtask(request, user_id):
        title = request.POST['title']
        desc = request.POST['description']
        due_date = request.POST['due_date']
        user = get_object_or_404(User, id=user_id)

        if TemdieTask.objects.filter(title=title).exists():
                return render(request, 'result.html', {'result': "This title already exist"})
        else:
                task =  TemdieTask.objects.create(title=title, description=desc, due_date=due_date, user=user)
                task.save()
                return render(request, 'result.html', {'result': "Task added !!"})        

def addtag(request):
    name = request.POST['name']
    task_ids = request.POST.getlist('tasks')

    task_ids = [int(task_id) for task_id in task_ids if task_id.isdigit()]

    tag = TemdieTag.objects.create(name=name)
    
    for task_id in task_ids:
        task = TemdieTask.objects.get(id=task_id)
        tag.task.add(task)

    return render(request, 'result.html', {'result': "Tag added !!"})

def deletetask(request, task_id):
    task = TemdieTask.objects.get(id=task_id)
    #task.temdietag_set.all().delete()
    task.delete()

    return render(request, 'result.html', {'result': "Task deleted !!"})


