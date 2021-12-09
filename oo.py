class Filmes:

    def __init__(self, nome, ano, duracao):
        self.__nome = nome
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()


como_treinar_seu_dragao = Filmes("como treinar seu dragao", 2017, 100)
como_treinar_seu_dragao.dar_like()
como_treinar_seu_dragao.dar_like()
como_treinar_seu_dragao.dar_like()
print(f"Nome: {como_treinar_seu_dragao.nome}, Ano: {como_treinar_seu_dragao.ano}, "
      f"Duracao: {como_treinar_seu_dragao.duracao}")


class Series:

    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()


the_witcher = Series("the witcher", 2019, 2)
the_witcher.dar_like()
the_witcher.dar_like()
print(f"Nome: {the_witcher.nome}, Ano: {the_witcher.ano}, Temporadas: {the_witcher.temporadas}")
