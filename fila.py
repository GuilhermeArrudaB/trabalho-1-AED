
class FilaEspera:
    def __init__(self):
        self.items = []

    def adicionar_na_fila(self, apartamento):
        self.items.append(apartamento)

    def retirar_da_fila(self):
        if not self.esta_vazia():
            return self.items.pop(0)
        else:
            return None

    def esta_vazia(self):
        return self.items == []

    def tamanho(self):
        return len(self.items)

    def imprimir(self):
        if len(self.items) == 0:
            print('A fila de espera está vazia.')
        else:
            print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')
            print('Fila de espera por vagas de garagem:')
            for apartamento in self.items:
                print(f'Apartamento {apartamento.numero}, Torre {apartamento.torre.nome}')
            print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')