
class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.inicio = None # Apartamento
        self.fim = None
        self.tamanho = 6

    def adicionar(self, valor):
        if self.inicio:
            aux = self.inicio
            while (aux.proximo):
                aux = aux.proximo
            aux.proximo = No(valor)
        else:
            self.inicio = No(valor)
        self.tamanho = self.tamanho + 1

    def imprimir(self):
        if self.inicio is None:
            print("Lista Vazia")
        else:
            aux = self.inicio
            while aux:
                print(aux.dado, "\n")
                aux = aux.proximo
            print("Tamanho da Lista: " + str(self.tamanho))

    def excluir(self, valor):
        if self.tamanho == 0 :
            print("A lista está vazia")
        elif self.tamanho == 1:
            if self.inicio.dado == valor:
                self.inicio = None
                self.tamanho -= 1
            else:
                print("Valor não encontrado")
        else:
            aux = self.inicio
            if self.inicio.dado == valor:
                aux = self.inicio.proximo
                self.inicio = aux
                self.tamanho -= 1
            else:
                ant = self.inicio
                aux = ant.próximo
                while (aux):
                    if aux.dado == valor:
                        ant.proximo = aux.próximo
                        self.tamanho -= 1
                    else:
                        ant = aux
                        aux = aux.proximo
