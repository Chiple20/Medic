from django.shortcuts import render
from .models import User
from django.db import IntegrityError
def index(request):
    return render(request,'index.html',{})
def QuienesSomos(request):
    return render(request,'Quienessomos.html',{})
def login(redirect):
    context={}
    return redirect(request, 'accounts/login.html', context)
#Crud Usuario
def registro(request):
    print("Hola estamos en la ventana index")
    return render(request, 'registration/registro.html', {})
def agregar_usuario(request):
    print("hola  estoy en agregar_figura...")
    if request.method == 'POST':
        var_usuario = request.POST['username']
        var_contraseña  = request.POST['password']
        var_email = request.POST['email']
        var_nombre = request.POST['first_name']
        var_apellido = request.POST['last_name']
        if var_usuario != "":
            try:
               usuario = User()
               usuario.username   = var_usuario
               usuario.email      = var_email 
               usuario.set_password(var_contraseña)
               usuario.first_name = var_nombre
               usuario.last_name  = var_apellido
               usuario.save()
               return render( request,'registration/agregado_corr.html',{})

            except IntegrityError:
               return render(request, 'registration/existe.html', {})
        else:
           return render(request, 'registration/vacio.html', {})
    else:
        return render(request, 'registration/noexiste.html', {})
