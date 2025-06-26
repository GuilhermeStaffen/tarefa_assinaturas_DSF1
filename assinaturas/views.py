from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Assinatura
from .forms import AssinaturaForm

def nova_assinatura(request):
    if request.method == 'POST':
        form = AssinaturaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Assinatura criada com sucesso!')
            return redirect('lista_assinaturas')
    else:
        form = AssinaturaForm()
    return render(request, 'assinaturas/nova_assinatura.html', {'form': form})

def lista_assinaturas(request):
    assinaturas = Assinatura.objects.all()
    return render(request, 'assinaturas/lista_assinaturas.html', {'assinaturas': assinaturas})

def assinatura_por_clientes(request, assinatura_id):
    assinatura = get_object_or_404(Assinatura, id=assinatura_id)
    clientes = assinatura.clientes.all()
    return render(request, 'assinaturas/assinatura_por_clientes.html', {
        'assinatura': assinatura,
        'clientes': clientes
    })