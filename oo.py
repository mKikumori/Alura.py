class Programa:

    def __init__(self, nome, ano):
        self._nome = nome
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f"{self.nome}, {self.ano}, {self.likes}"

class Filmes(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f"{self.nome}, {self.ano}, {self.duracao} min, {self.likes} likes"


class Series(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"{self.nome}, {self.ano}, {self.temporadas} temporadas, {self.likes} likes"


class Playlist:

    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)

como_treinar_seu_dragao = Filmes("como treinar seu dragao", 2017, 100)
the_witcher = Series("the witcher", 2019, 2)
friends = Series("friends", 2005, 7)
transformers = Filmes("transformers", 2012, 150)
como_treinar_seu_dragao.dar_like()
como_treinar_seu_dragao.dar_like()
como_treinar_seu_dragao.dar_like()
the_witcher.dar_like()
the_witcher.dar_like()
friends.dar_like()
friends.dar_like()
transformers.dar_like()
transformers.dar_like()


filmes_e_series = [como_treinar_seu_dragao, the_witcher, friends, transformers]
minha_playlist = Playlist("Fim de semana", filmes_e_series)

for programa in minha_playlist.listagem:
    print(programa)

print(f'Tamanho: {len(minha_playlist.listagem)}')
