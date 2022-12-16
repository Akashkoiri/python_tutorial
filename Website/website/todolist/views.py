from django.shortcuts import render
from django.views import View 
from .forms import ListForm

# Create your views here.


class TodoList(View):

    list = []

    def get(self, request):
        form = ListForm()
        list = TodoList.list
        return render(request, 'todolist/list.html', {'form':form, 'list':list})
        

    def post(self, request):
        form = ListForm(request.POST)
        list = TodoList.list
        list.append(request.POST.get('name'))
        return render(request, 'todolist/list.html', {'form':form, 'list':list})



