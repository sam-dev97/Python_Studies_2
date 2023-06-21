import contas


# Criação da classe Pessoa
class Pessoa():
    # Pessoa tem: nome e idade
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    # Definindo um getter para nome como solicitado no exercício
    @property
    def nome(self):
        return self._nome

    # Definindo um setter como solicitado no exercício
    @nome.setter
    def nome(self, nome: str):
        self._nome = nome

    # Definindo um getter para idade como solicitado no exercício
    @property
    def idade(self):
        return self._idade

    # Definindo um setter como solicitado no exercício
    @idade.setter
    def idade(self, idade: int):
        self._idade = idade

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.nome!r}, {self.idade!r})'
        return f'{class_name} {attrs}'


# Classe cliente herda de Pessoa, pois um Cliente é uma Pessoa
class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta: contas.Conta | None = None


if __name__ == '__main__':
    c1 = Cliente('Luiz', '18')
    c1.conta = contas.ContaCorrente(111, 222, 0, 0)
    print(c1)
    print(c1.conta)

    c2 = Cliente('Maria', '22')
    c2.conta = contas.ContaPoupanca(123, 456, 500)
    print(c2)
    print(c2.conta)
