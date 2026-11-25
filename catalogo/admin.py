from django.contrib import admin

from .models import Autor, Genero, Livro

admin.site.register(Autor)
admin.site.register(Genero)


class LivroAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "genero", "ano")
    list_filter = ("autor", "genero")
    search_fields = ("titulo",)


admin.site.register(Livro, LivroAdmin)
