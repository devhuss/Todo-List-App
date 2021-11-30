from django.shortcuts import render, redirect

from .models import Todo
from .forms import TodoForm


def index(request):
    todo_list = Todo.objects.all()
    form = TodoForm()
    context = {'todo_list' : todo_list, 'form' : form}
    return render(request, 'todo/index.html', context)



def addTodo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        
        form.save()

        return redirect('index')

    return render(request, 'todo/update.html', {'form': form})




    
def update(request, id):
    task = Todo.objects.get(id=id)
    form = TodoForm(request.POST or None, instance=task)

   
    if form.is_valid():
        form.save()
       
        
        return redirect('index')

    form = TodoForm(instance=task)
    return render(request, 'todo/update.html', {'form': form})


def delete(request, id):
    
    todo = Todo.objects.get(id=id)
    if request.method == 'POST':

        todo.delete() 

        return redirect('index')
    context = {'todo': todo}
    return render(request, 'todo/delete.html', context)


 	    
def completeTodo(request, id):
    todo = Todo.objects.get(id=id)
    todo.complete = True
    todo.save()

    return redirect('index')

def updateTodo(request, id):
    todo = Todo.objects.get(id=id)
    todo.updated= True
    todo.save()

    
    

    return redirect('index')
     
        