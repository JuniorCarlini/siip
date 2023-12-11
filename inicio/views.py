from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from .forms import ProprietarioForm
from .models import Proprietario , Armadilha , Propriedade

@login_required(login_url='login')  # Substitua 'login' pela URL da sua tela de login
def index(request):

    # busca as informações do banco de dados para mostrar na página inicial
    total_usuarios = Proprietario.objects.count()
    total_propriedades = Propriedade.objects.count()
    total_armadilhas = Armadilha.objects.count()
    
    armadilhas = Armadilha.objects.all()
    return render(request, 'inicio/index.html',{'armadilhas': armadilhas,
        'total_usuarios': total_usuarios,
        'total_armadilhas': total_armadilhas,
        'total_propriedades': total_propriedades,})

@login_required(login_url='login')  # Substitua 'login' pela URL da sua tela de login
def proprietarios(request):
    form = ProprietarioForm()
    
    proprietarios_list = Proprietario.objects.all()

    # Configurando a paginação
    paginator = Paginator(proprietarios_list, 15)
    page = request.GET.get('page')

    try:
        proprietarios = paginator.page(page)
    except PageNotAnInteger:
        proprietarios = paginator.page(1)
    except EmptyPage:
        proprietarios = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        form = ProprietarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(request.path)

    return render(request, 'inicio/proprietarios.html',{'form': form, 'proprietarios': proprietarios})