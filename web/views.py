from django.shortcuts import render, redirect
from .forms import ContactFormForm, MiForm
from .models import Flan 
from django.contrib.auth import logout
from django.contrib.auth import login


def index(request):

    flanes_publicos = Flan.objects.filter(is_private=False)

    dict={
        'titulo':'Bienvenidos a Onlyflans',
        'Is_loggin':True,
        'sesion':3,
        'flanes_publicos':flanes_publicos,
    }
    return render(request, 'index.html', dict)

def about(request):
    context={
        'is_loggin':True,
    }
    return render(request, 'about.html', context)

def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    context={
        'is_loggin':True,
        'flanes_privados':flanes_privados,
    }
    return render(request, 'welcome.html', context)

def logged_out(request):
        logout(request)
        return redirect('/')


def contact(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exito')

    formulario=ContactFormForm()
    contexto={
        'formulario':formulario,
    }

    return render(request, 'contact.html', contexto)




def exito(request):
    return render(request, 'exito.html')