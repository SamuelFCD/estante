from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Autor, Genero, Livro


def lista_livros(request):
    livros = Livro.objects.all()

    # pega o que veio na URL (formulário com method GET)
    busca = request.GET.get("busca", "")
    autor = request.GET.get("autor", "")
    genero = request.GET.get("genero", "")

    # cada filtro só é aplicado se o usuário preencheu
    if busca:
        livros = livros.filter(titulo__icontains=busca)
    if autor.isdigit():
        livros = livros.filter(autor__id=autor)
    if genero.isdigit():
        livros = livros.filter(genero__id=genero)

    livros = livros.order_by("titulo", "id")

    # a paginação vem depois dos filtros
    paginator = Paginator(livros, 5)
    numero_pagina = request.GET.get("page")
    page_obj = paginator.get_page(numero_pagina)

    return render(request, "catalogo/lista.html", {
        "page_obj": page_obj,
        "autores": Autor.objects.all(),
        "generos": Genero.objects.all(),
        "busca": busca,
        "autor_selecionado": autor,
        "genero_selecionado": genero,
    })
