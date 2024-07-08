torres = []


class Torre:
    id_counter = 0

    def __init__(self, nome, endereco):
        self.id = Torre.id_counter
        self.nome = nome
        self.endereco = endereco
        self.apartamentos = []
        Torre.id_counter += 1

    def __str__(self):
        return f"ID: {self.id}, Nome: {self.nome}, Endereço: {self.endereco}\n"


#teste main
