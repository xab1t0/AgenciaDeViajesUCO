from django.shortcuts import render, render_to_response, loader, HttpResponse
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.template.context import RequestContext
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm
from Usuario.models import Usuario

# View que permite el registro de un nuevo usuario
def nuevo_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            usuario = request.POST['username']
            user = User.objects.get(username=usuario)
            cliente = Usuario.objects.create(nombre_Usuario=usuario, usuario=user)
            cliente.save()
            return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()
    template = loader.get_template('Usuario/registro.html')
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))

# View que permite el login de un cliente
def ingresar(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                login(request, acceso)
                return HttpResponseRedirect('/')
            else:
                return render(request, 'Usuario/incorrecto.html')
    else:
        form = AuthenticationForm()
    template = loader.get_template('Usuario/login.html')
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))

# View que permite el logout de un cliente, vista solo permitida para clientes ya logueados
@login_required(login_url='/ingreso')
def cerrarSesion(request):
    logout(request)
    return HttpResponseRedirect('/')

# View que permite ver el perfil del cliente
def perfil(request, usuario_id):
    usuario = request.user.id
    cliente = Usuario.objects.get(pk=usuario_id)

    #user = User.objects.get(username=usuario)
    id_cliente = cliente.usuario.id
    template = loader.get_template('Usuario/perfil.html')
    context = {
        'cliente': cliente,
        'id_cliente':id_cliente,
        'usuario': usuario,
    }
    return HttpResponse(template.render(context, request))
