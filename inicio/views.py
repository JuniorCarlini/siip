from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from .forms import ProprietarioForm
from .models import Proprietario

def index(request):
    return render(request, 'inicio/index.html')

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