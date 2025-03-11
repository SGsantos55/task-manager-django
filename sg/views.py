from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Todo
from .forms import createtodo
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

def sign(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if User.objects.filter(username=username).exists():  
                messages.error(request, "Username already taken.")
            else:
                user = User.objects.create_user(username=username, password=password1)  
                user.save()
                messages.success(request, "Account created successfully.")
                return redirect('home') 
        else:
            messages.error(request, "Passwords do not match.")

    return render(request, 'sign.html')
def login_user(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(username=username , password = password)
        if user is not None:
            login(request,user)
            return redirect('Todo_list')
        else:
            messages.error(request, "Invalid username or password")
    return render(request,'home.html')
def santos(request):
    if request.user.is_anonymous:
        return redirect('login_user')
    
    return render(request,'santos.html')
def logout_user(request):
    logout(request)
    return redirect('home')

def Todo_list(request):
    if request.user.is_anonymous:
        return redirect('login_user')
    todos = Todo.objects.filter(user=request.user)  #  Show only logged-in user's todos
    available_tasks = todos.filter(completed=False).count()
    finished_tasks = todos.filter(completed=True).count()
    data = {
        'todos': todos,
        'available_tasks': available_tasks,
        'finished_tasks': finished_tasks
    }
    return render(request, 'todo_list.html', data)  #  Pass the data to the template  
@login_required(login_url='login_user')
def create_todo(request):
    form = createtodo()
    if request.method == 'POST':
        form = createtodo(request.POST)
        if form.is_valid():
           sg=form.save(commit=False)
           sg.user = request.user
           sg.save()
           return redirect('Todo_list')

           
    return render(request,'createtodo.html',{'form':form})
@login_required(login_url='login_user')
def update_todo(request,pk):
    todo=Todo.objects.get(id=int(pk))
    form=createtodo(instance =todo)
    if request.method =='POST':
        if todo.user==request.user:
            form=createtodo(request.POST,instance=todo)
            if form.is_valid():
                form.save()
                return redirect('Todo_list')
        else:
            messages.error(request, "This is not your todo.")


    return render(request,'createtodo.html',{'form' : form})
@login_required(login_url='login_user')
def delete_todo(request,pk):
    todo=Todo.objects.get(id=pk)
    if todo.user==request.user:
        todo.delete()
        return redirect('Todo_list')
      
       
    return render(request,'delete.html',{'todo':todo})