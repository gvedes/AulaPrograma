from django.shortcuts import render, redirect
from .models import Saidas
from .forms import SaidaForm

def list_saida(request):
    saidas = Saidas.objects.all()
    template_name = 'list_saida.html'
    context = {'saidas': saidas}
    return render(request, template_name, context)


def new_saida(request):
    if request.method == 'POST':
        form = SaidaForm(request.POST)
        if form.is_valid():
            saida = form.save(commit=False)
            produto = form.cleaned_data['produto']
            quantidade = form.cleaned_data['quantidade']
            if quantidade > produto.quantidade:
                return render(request, 'erro_saida.html')
            produto.quantidade -= quantidade
            produto.save()
            saida.save()
            return redirect('saida:list_saida')
    return render(request, 'new_saida.html', {'form': SaidaForm()})



def update_saida(request, pk):
    saida = Saidas.objects.get(pk=pk)
    produto = saida.produto
    estoque_original = produto.quantidade + saida.quantidade

    if request.method == 'POST':
        form = SaidaForm(request.POST, instance=saida)

        if form.is_valid():
            nova_qtd = form.cleaned_data['quantidade']
            if nova_qtd <= 0:
                return render(request, 'erro_saida.html')
            if nova_qtd > estoque_original:
                return render(request, 'erro_saida.html')
            produto.quantidade = estoque_original - nova_qtd
            produto.save()
            form.save()

            return redirect('saida:list_saida')

    else:
        form = SaidaForm(instance=saida)

    context = {'form': form, 'pk': pk}
    return render(request, 'update_saida.html', context)
def delete_saida(request, pk):
    saida = Saidas.objects.get(pk=pk)
    
    if request.method == 'POST':
        saida.produto.quantidade = saida.produto.quantidade + saida.quantidade
        saida.produto.save()
        saida.delete()
        return redirect('saida:list_saida')
    
    template_name = 'delete_saida.html'
    context = {
        'saida' : saida,
    }
    
    return render(request, template_name, context)