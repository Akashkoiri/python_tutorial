from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    
    path('', include('django.contrib.auth.urls')),

    path('app1/', include('app1.urls')),
    path('register/', views.Register.as_view(), name='register'),
    path('todolist/', include('todolist.urls')),
]
