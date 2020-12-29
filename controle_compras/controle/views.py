from django.shortcuts import render
from controle.forms import CategoriaForm


def categoria_adicionar(request):
    template = 'controle/categoria/adicionar.html'
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            pass
    context = {
        'form': CategoriaForm()
    }
    return render(request, template, context)



