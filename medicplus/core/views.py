from django.shortcuts import render
from .models import User
from django.db import IntegrityError
from .models import FormularioConsulta
def index(request):
    return render(request,'index.html',{})
def solicitado(request):
    return render(request,'solicitado.html',{})
    
def QuienesSomos(request):
    return render(request,'Quienessomos.html',{})
def login(redirect):
    context={}
    return redirect(request, 'accounts/login.html', context)
#Crud Usuario
def registro(request):
    print("Hola estamos en la ventana index")
    return render(request, 'registration/registro.html', {})

#agregar solicitud 
def Formulario(request):
    return render(request,'Formulario.html',{})

def agregar_solicitud (request):
    print("hola  estoy en agregar producto...")
    if request.method == 'POST':
        mi_id_formulario=request.POST["id_formulario"]
        mi_motivo_consulta = request.POST['motivo_consulta']
        mi_fc_id_ficha = request.POST['fc_id_ficha']
        mi_sintoma = request.POST['sintoma']
        mi_prioridad = request.POST['prioridad']
        mi_hora = request.POST['hora_solicitud']
       
        if mi_id_formulario != "":
            try:
                
                Consulta = FormularioConsulta()
                Consulta.id_formulario=mi_id_formulario
                Consulta.motivo_consulta = mi_motivo_consulta
                Consulta.fc_id_ficha = mi_fc_id_ficha
                Consulta.sintoma = mi_sintoma
                Consulta.prioridad = mi_prioridad
                Consulta.hora_solicitud=mi_hora
                Consulta.save()
                return render(request, 'solicitado.html', {})
            except Consulta.DoesNotExist:
                return render(request, 'core/error/error_204.html', {})
        else:
            return render(request, 'core/error/error_201.html', {})
    else:
        return render(request, 'core/error/error_203.html', {})



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

def listado(request):
    print("estamos al aire tulio lista de espera")
    #lista = Alumno.objects.all()
    lista = FormularioConsulta.objects.all()
    context={'listado':lista}
    return render(request,'listado.html',context)