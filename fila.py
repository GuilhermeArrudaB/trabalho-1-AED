
class FilaEspera:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def adicionar(self, apartamento):
        if self.fim is None:
            self.inicio = apartamento
        else:
            self.fim.proximo = apartamento
        self.fim = apartamento
        self.tamanho += 1
        print(f'Tamanho da fila {self.tamanho}')

    def remover(self):
        if self.tamanho > 0:
            auxiliar = self.inicio
            self.inicio = auxiliar.proximo
            auxiliar.proximo = None
            self.tamanho -= 1
            if self.tamanho == 0:
                self.fim = None
        else:
            print("A lista está vazia.")

    def imprimir(self):
        if self.tamanho == 0:
            print('A fila de espera está vazia.')
        else:
            apartamentos = []
            auxiliar = self.inicio
            qtd_apartamentos = 1
            print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')
            print('Fila de espera por vagas de garagem:')

            while auxiliar:
                apartamentos.append(f"Posição {qtd_apartamentos}: {auxiliar}")
                auxiliar = auxiliar.proximo
                qtd_apartamentos += 1

            print("\n".join(apartamentos))
            print(f"{self.tamanho} apartamento(s) na lista de espera.")
            print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')