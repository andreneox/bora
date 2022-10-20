from curses.ascii import isdigit
from distutils.log import info
from re import A
from django.shortcuts import redirect, render
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from django.contrib.auth.decorators import login_required

from boraApp.models import Lugar, Agendamento


# Create your views here.


def home(request):
    return render (request, "home.html")

@login_required(login_url='/login' )
def lugar(request):
    lugares = Lugar.objects.all()

    context = {
        'lugares' : lugares
    }
    return render (request, 'quadra.html', context)

def login(request):
    if request.method =='GET':
        return render (request, "login.html")
    else :
        username = request.POST.get('usuario')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)
        if user :
            login_django(request, user)
            return render (request, 'home.html')
        else :
            messages.info(request, 'Usuario ou senha invalidos!')
            return redirect ('login')


def logout(request):
    logout_django (request)
    messages.info(request, "Voce esta deslogado com sucesso.") 
    return redirect("home") 



def cadastro(request):
    if request.method == "GET":
        return render (request, "cadastro.html")
    else: 
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        username = request.POST.get('usuario')
        senha = request.POST.get('senha')
        count_nums = 0
        # checagem de numeros
        for c in nome :
            if c.isdigit():
                count_nums+=1
        if count_nums > 0 :
            messages.info (request, 'O nome deve conter apenas letras')
            return redirect ('cadastro')
        if len(nome.strip()) ==0 or len(email.strip()) == 0 or len (username.strip()) == 0 :
            messages.info (request, 'Favor inserir os dados corretamente')
            return redirect ('cadastro')
        if len (senha) < 6 or len (senha) > 10 :
            messages.info ( request, 'Favor inserir uma senha entre 6 a 10 caracteres')
            return redirect ('cadastro')

        #contadores
        count_alpha = 0
        count_nums = 0

        #checagem de caracteres
        for c in senha:
            if c.isalpha():
                count_alpha +=1
            elif c.isdigit():
                count_nums += 1
        if count_alpha == 0 or count_nums == 0 :
            messages.info ('A senha deve contar com letras e numeros')
            return redirect('cadastro') 
        user = User.objects.filter(email=email).first()
    if user :
            messages.info(request, 'Esse email de usuario ja esta cadastrado em nosso sistema!') 
            return redirect ('cadastro') 
    else :
            user = User.objects.filter(username=username).first()
            if user :
                messages.info (request, 'Ja existe um usuario com esse username') 
                return redirect ('cadastro')
            else :
                user = User.objects.create_user(first_name = nome, last_name = sobrenome, email = email, username = username, password = senha)
                user.save()
                messages.info (request, 'Usuario cadastrado com sucesso!')
                return redirect  ('home') 
        #return HttpResponse(username)  



def quadra_add(request):
    quadras = Lugar.objects.all()
    if request.method == "GET":
        return render (request, "quadra_add.html")
    else :
        nome = request.POST.get ('nome')
        endereco =  request.POST.get ('endereco')
        esporte =  request.POST.get ('esporte') 

        lugar = Lugar.objects.filter(nome=nome).first()
        if lugar :
            messages.info(request, 'Essa quadra ja esta cadastrada em nosso sistema!')     
            return redirect ('quadra_add')
        else :
            lugar = Lugar(nome=nome, endereco=endereco, esporte=esporte)
            lugar.save()
            messages.info (request, 'Quadra cadastrada com sucesso!')
            return redirect ('quadra')  


def quadra (request):
    lugares = Lugar.objects.all()

    context = {
        'lugares' : lugares
    }
    return render (request, 'quadra.html', context)
                  

def agendar (request):
    if request.method == "GET":
        lugares = Lugar.objects.all()
        context = {
            "quadras":lugares
        }                 
        return render (request, 'agendamento_add.html', context)
    else:
        quadra = request.POST.get('quadra')
        #quadra = Lugar.objects.get(id=nome)
        localidade = request.POST.get('localidade')
        #localidade = Lugar.objects.get(id=endereco)
        inicio = request.POST.get('inicio')
        fim = request.POST.get('fim')


        buscaInicio = Agendamento.objects.filter(inicio=inicio).first()
        if buscaInicio: 
            messages.info(request, 'Esse horario ja foi agendado!')
            return redirect('agendamento')
        else:
            agendamento = Agendamento(quadra=quadra, localidade=localidade, inicio=inicio, fim=fim )
            agendamento.save()
            messages.info(request,'Agendamento Realizado com Sucesso!')
            return redirect('agenda')

