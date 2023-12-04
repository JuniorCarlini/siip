from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from .forms import ProprietarioForm
from .models import Proprietario

def index(request):
    return render(request, 'inicio/index.html')

def proprietarios(request):
    form = ProprietarioForm()

    # Obtendo todos os proprietários do banco de dados
    proprietarios_list = Proprietario.objects.all()

    # Obtendo todos os proprietários do banco de dados
    proprietarios_list = Proprietario.objects.all()

        # Configurando a paginação
    paginator = Paginator(proprietarios_list, 15)  # 30 itens por página
    page = request.GET.get('page')

    try:
        proprietarios = paginator.page(page)
    except PageNotAnInteger:
        # Se a página não é um número inteiro, entrega a primeira página.
        proprietarios = paginator.page(1)
    except EmptyPage:
        # Se a página está fora do intervalo (por exemplo, 9999), entrega a última página de resultados.
        proprietarios = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        form = ProprietarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(request.path)

    return render(request, 'inicio/proprietarios.html',{'form': form, 'proprietarios': proprietarios})

 #   return render(request, 'inicio/proprietarios.html', {'form': form, 'proprietarios': proprietarios})
