
class ListaEncadeada:
    def __init__(self, valor=None):
        self.primeiro = valor
        self.proximo = None

    def adicionar(self, valor):
        novo_no = ListaEncadeada(valor)
        if self.primeiro is None:
            self.primeiro = novo_no
        else:
            atual = self.primeiro
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_no

    def imprimir(self):
        atual = self.primeiro
        while atual is not None:
            print(atual.valor)
            atual = atual.proximo