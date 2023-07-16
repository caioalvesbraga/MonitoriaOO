from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddAlunoForm
from .models import Aluno

# Neste arquivo são definidas as funções que realizam o CRUD
def home(request):
    alunos = Aluno.objects.all()

    ##Verifica se o usuário está logando no site
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login realizado com sucesso!")
            return redirect('home')
        else:
            messages.success(request, "Houve um erro ao logar. Tente novamente...")
            return redirect('home')
    
    #Caso não esteja logando, apenas vá para a página inicial
    else:
        return render(request, 'home.html', {'alunos':alunos})

def logout_user(request):
    logout(request)
    messages.success(request, "Você saiu da sua conta")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Conta cadastrada com sucesso. Seja bem-vindo!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form' : form})
    
    return render(request, 'register.html', {'form' : form})

def customer_aluno(request, pk):
    if request.user.is_authenticated:
        customer_aluno = Aluno.objects.get(id=pk)
        return render(request, 'aluno.html', {'customer_aluno' : customer_aluno})
    else:
        messages.success(request, "Você precisa estar logado para visualizar esta página!")
        return redirect('home')
    
def deletar_aluno(request, pk):
    if request.user.is_authenticated:
        delete_it = Aluno.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Aluno removido com sucesso!")
        return redirect('home')
    else:
        messages.success(request, "Você precisa estar logado para visualizar esta página!")
        return redirect('home')

def add_aluno(request):
    form = AddAlunoForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                aluno = form.save()
                messages.success(request, "Aluno adicionado com sucesso!")
                return redirect('home')
        return render(request, 'add_aluno.html', {'form' : form})
    else:
        messages.success(request, "Você precisa estar logado para visualizar esta página!")
        return redirect('home')
    

def update_aluno(request, pk):
   if request.user.is_authenticated:
       aluno_atual = Aluno.objects.get(id=pk)
       form = AddAlunoForm(request.POST or None, instance=aluno_atual)
       if form.is_valid():
            form.save()
            messages.success(request, "O Aluno foi editado com sucesso")
            return redirect('home')
       return render(request, 'update_aluno.html', {'form' : form})
   else:
        messages.success(request, "Você precisa estar logado para visualizar esta página!")
        return redirect('home')
