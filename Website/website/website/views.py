from django.shortcuts import render
from django.views import View
from .forms import RegisterForm
from django.contrib import auth

def home(request):
    return render(request, 'base.html')




class Register(View):

    def get(self, request):
        form = RegisterForm()
        return render(request, 'registration/register2.html', {'form':form})
    
    def post(self, request):
        form = RegisterForm(request.POST).cleaned_data
        # print(request.POST['username'])
        # user = form.Meta.model().create_user()
        # print(user)
        # if form.is_valid():
            # user = form.save()  # Sujal
            # auth.login(request, user)
        return render(request, 'registration/register2.html', {'form':form})

