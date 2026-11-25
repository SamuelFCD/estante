from django.core.management.base import BaseCommand

from catalogo.models import Autor, Genero, Livro

# (título, ano, autor, gênero)
LIVROS = [
    ("Helena", 1876, "Machado de Assis", "Romance"),
    ("Memórias Póstumas de Brás Cubas", 1881, "Machado de Assis", "Romance"),
    ("Papéis Avulsos", 1882, "Machado de Assis", "Contos"),
    ("Quincas Borba", 1891, "Machado de Assis", "Romance"),
    ("Várias Histórias", 1896, "Machado de Assis", "Contos"),
    ("Dom Casmurro", 1899, "Machado de Assis", "Romance"),
    ("Esaú e Jacó", 1904, "Machado de Assis", "Romance"),
    ("Perto do Coração Selvagem", 1943, "Clarice Lispector", "Romance"),
    ("Laços de Família", 1960, "Clarice Lispector", "Contos"),
    ("A Paixão Segundo G.H.", 1964, "Clarice Lispector", "Romance"),
    ("A Hora da Estrela", 1977, "Clarice Lispector", "Romance"),
    ("São Bernardo", 1934, "Graciliano Ramos", "Romance"),
    ("Angústia", 1936, "Graciliano Ramos", "Romance"),
    ("Vidas Secas", 1938, "Graciliano Ramos", "Romance"),
    ("Capitães da Areia", 1937, "Jorge Amado", "Romance"),
    ("Gabriela, Cravo e Canela", 1958, "Jorge Amado", "Romance"),
    ("Dona Flor e Seus Dois Maridos", 1966, "Jorge Amado", "Romance"),
    ("Eu, Robô", 1950, "Isaac Asimov", "Ficção Científica"),
    ("Fundação", 1951, "Isaac Asimov", "Ficção Científica"),
    ("O Fim da Eternidade", 1955, "Isaac Asimov", "Ficção Científica"),
    ("O Assassinato de Roger Ackroyd", 1926, "Agatha Christie", "Policial"),
    ("Assassinato no Expresso do Oriente", 1934, "Agatha Christie", "Policial"),
    ("E Não Sobrou Nenhum", 1939, "Agatha Christie", "Policial"),
]


class Command(BaseCommand):
    help = "Cadastra autores, gêneros e livros de exemplo"

    def handle(self, *args, **options):
        for titulo, ano, nome_autor, nome_genero in LIVROS:
            autor, _ = Autor.objects.get_or_create(nome=nome_autor)
            genero, _ = Genero.objects.get_or_create(nome=nome_genero)
            Livro.objects.update_or_create(
                titulo=titulo,
                defaults={"ano": ano, "autor": autor, "genero": genero},
            )
        self.stdout.write("Livros cadastrados: %d" % Livro.objects.count())
