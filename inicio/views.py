from django.shortcuts import render , redirect
from .forms import ProprietarioForm

def index(request):
    return render(request, 'inicio/index.html')

def proprietarios(request):
    form = ProprietarioForm()

    if request.method == 'POST':
        form = ProprietarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(request.path)

    return render(request, 'inicio/proprietarios.html', {'form': form})