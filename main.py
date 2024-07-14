from menu import cadastrar_apartamento, cadastrar_torre, liberar_vaga, lista_espera, mostrar_vagas
from fila import FilaEspera
from lista import ListaEncadeada
from apartamento import Apartamento
from torre import Torre, torres
escolha = None


class Sistema:
    def __init__(self):
        self.fila_de_espera = FilaEspera()
        self.vagas_ocupadas = ListaEncadeada()


sistema = Sistema()
torre = Torre('B1', 'Rua Marista')
torre2 = Torre('B2', 'Rua Catarina')
ap1 = Apartamento(201, 1, torre)
ap2 = Apartamento(202, 2, torre)
ap3 = Apartamento(203, 3, torre)
ap4 = Apartamento(101, None, torre2)

sistema.vagas_ocupadas.adicionar(ap1)
sistema.vagas_ocupadas.adicionar(ap2)
sistema.vagas_ocupadas.adicionar(ap3)

torres.append(torre)
torre.apartamentos.append(ap1)
torre.apartamentos.append(ap2)
torre.apartamentos.append(ap3)


while escolha != 6:

    print('Sistema Auxiliadora Predial\n'
          '    Menu de opções:    \n'
          '1) Cadastrar apartamento\n'
          '2) Cadastrar torre\n'
          '3) Liberar vaga\n'
          '4) Apartamentos que possuem vagas\n'
          '5) Lista de espera por vagas\n'
          '6) Sair\n')
    try:
        escolha = int(input('Digite o que deseja: '))
        if escolha == 6:
            break
        elif escolha < 1 or escolha > 6:
            print('Digite um número válido!\n')
        elif escolha == 1:
            cadastrar_apartamento(sistema)
        elif escolha == 2:
            cadastrar_torre()
        elif escolha == 3:
            liberar_vaga(sistema)
        elif escolha == 4:
            mostrar_vagas(sistema)
        elif escolha == 5:
            lista_espera(sistema)
        else:
            print('Opção não encontrada\n')

    except Exception as e:
        print('Digite um número!')
        print(f'Código de erro: {e}\n')



