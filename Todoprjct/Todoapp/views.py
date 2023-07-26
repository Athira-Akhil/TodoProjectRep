from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . models import Task
from . forms import TodoForm

# Class based generic views
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

# Create your class based generic views here.
class TaskListView(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task1'

class TaskDetailView(DetailView):
    model=Task
    template_name = 'detail.html'
    context_object_name = 'task'

class TaskUpdateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class TaskDeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')

# Create your function based views here.
def addtask(request):
    task1 = Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(request, 'home.html',{'task1':task1})


def delete(request,taskid):
    if request.method=='POST':
        task_id=Task.objects.get(id=taskid)
        task_id.delete()
        return redirect('/')
    return render(request,'delete.html')

def updatetask(request,taskid1):
     taskid=Task.objects.get(id=taskid1)
     taskform=TodoForm(request.POST or None,instance=taskid)
     if taskform.is_valid():
         taskform.save()
         return redirect('/')
     return render(request,'edit.html',{'taskform':taskform,'taskid':taskid})

