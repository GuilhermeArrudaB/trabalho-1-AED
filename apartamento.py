from torre import Torre


class Apartamento:
    id_counter = 0

    def __init__(self, numero, vaga, torre=None):
        self.id = Apartamento.id_counter
        self.numero = numero
        self.torre = torre
        self.vaga = vaga
        self.proximo = None # Apartamento
        Apartamento.id_counter += 1

    def __str__(self):
        return f"ID: {self.id}, Número {self.numero}, Torre: {self.torre}, Número vaga: {self.vaga}"

