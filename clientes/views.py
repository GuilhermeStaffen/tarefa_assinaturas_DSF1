from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ClienteForm
from django.db.models import Q

def cadastro_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'clientes/cadastro_clientes.html', {'form': form})

def lista_clientes(request):
    busca = request.GET.get('busca', '')
    if busca:
        clientes = Cliente.objects.filter(nome__icontains=busca)
    else:
        clientes = Cliente.objects.all()
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})
