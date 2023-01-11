from django.shortcuts import render, redirect
from django.views import View

# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, 'chat/index.html')
    
    def post(self, request):
        request.session['username'] = str(request.POST['username'])
        return redirect('lobby/')


def lobby(request):
    return render(request, 'chat/lobby.html')

