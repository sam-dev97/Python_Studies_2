from abc import ABC, abstractmethod


# Classe abstrata, que deve ser implementado nas classes Corrente e Poupanca
class Conta(ABC):
    def __init__(self, agencia:  int, conta: int, saldo: float = 0):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    # Definição do método abstrato, como foi solicitado no exercício
    @abstractmethod
    def sacar(self, valor):
        ...

    def depositar(self, valor):
        self.saldo += valor
        self.detalhes(f'(DEPÓSITO {valor})')

    # Mostra o saldo do cliente e uma mensagem personalizada
    def detalhes(self, msg=''):
        print(f'O seu saldo é: {self.saldo:.2f} {msg}')
        print('--')

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r})'
        return f'{class_name} {attrs}'

# Herda de conta o método abstrato sacar

# ContaPoupanca herda de Conta


class ContaPoupanca(Conta):
    # Implementação do método abstrato sacar que foi herdado da classe Conta
    # Função sacar: retira fundos da ContaPoupanca
    def sacar(self, valor: float):
        valor_pos_saque = self.saldo - valor

        # Conta poupança não pode ter saldo negativo
        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return self.saldo
        print('Não foi possível sacar o valor desejado!')
        self.detalhes(f'(SAQUE NEGADO {valor})')

    # Função de depósito: adiciona saldo a ContaPoupanca
    def depositar(self, valor):
        self.saldo += valor
        self.detalhes(f'(DEPÓSITO {valor})')


# ContaCorrente herda de Conta
class ContaCorrente(Conta):
    def __init__(self, agencia: int, conta: int, saldo: float = 0, limite=0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite
    # Implementação do método abstrato sacar que foi herdado da classe Conta
    # Função sacar: retira fundos da ContaCorrente

    def sacar(self, valor: float):
        valor_pos_saque = self.saldo - valor
        # Podemos definir um limite negativo para a conta
        limite_maximo = -self.limite

        # Conta corrente pode ter saldo negativo
        if valor_pos_saque > limite_maximo:
            self.saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return self.saldo
        print('Não foi possível sacar! LIMITE MÁXIMO ATINGIDO')
        self.detalhes(f'(SAQUE NEGADO {valor})')

    # Função de depósito: adiciona saldo a ContaCorrente
    def depositar(self, valor: float):
        self.saldo += valor
        self.detalhes(f'(DEPÓSITO {valor})')

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r},'\
            f' {self.limite!r})'
        return f'{class_name} {attrs}'


if __name__ == '__main__':
    cc1 = ContaCorrente(111, 222, 0, 1000)
    cc1.sacar(100)
    cc1.depositar(500)
    cc1.sacar(200)
