from torre import torres, Torre
from apartamento import Apartamento
from fila import FilaEspera

def cadastrar_apartamento(sistema):
    if len(torres) == 0:
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')
        print('Cadastre uma torre antes de criar um apartamento!\n')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')
        return

    while True:
        print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')
        print('Cadastramento de novo apartamento: \n')
        try:
            num = int(input('Digite o número do apartamento:'))
            vagas = int(input('Digite o número da vaga do apartamento(1 a 10): \n'))

            if vagas > 10 or vagas < 0:
                print('Digite um número de 1 a 10!\n')
                print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')
                return

            print('\nTorres disponíveis: ')
            for torre in torres:
                print(torre)
            escolha = int(input('Digite o ID da torre do apartamento: '))
            torre = next((torre for torre in torres if torre.id == escolha), None)

            if torre:
                if sistema.vagas_ocupadas.tamanho < 10:
                    apartamento = Apartamento(num, vagas)
                    apartamento.torre = torre
                    print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
                    print('\nApartamento cadastrado:')
                    print(f'ID apartamento: {apartamento.id}\n'
                              f'Número: {apartamento.numero}\n'
                              f'Vagas: {apartamento.vaga}\n'
                              f'Torre:\n'
                              f'{torre}')
                    torre.apartamentos.append(apartamento)
                    sistema.vagas_ocupadas.adicionar(apartamento)

                    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')
                else:
                    apartamento = Apartamento(num, None, torre)
                    sistema.fila_de_espera.adicionar(apartamento)
                    print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
                    print('Apartamento adicionado à fila de espera: \n')
                    print(f'ID ap: {apartamento.id}\n'
                          f'Número: {apartamento.numero}\n'
                          f'Torre:\n'
                          f'{torre}')
                    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

            else:
                print('Essa torre não existe!')

            sair = input('Deseja encerrar? (S/N)').upper()
            if sair == 'S':
                print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')
                break

        except Exception as e:
            print('Digite valores validos!')
            print(f'Código de erro: {e}')



def cadastrar_torre():
    print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')
    nome = str(input('Digite o nome da torre:'))
    endereco = str(input('Digite o endereço da torre:'))
    torre = Torre(nome, endereco)
    torres.append(torre)
    print('Torre cadastrada com sucesso!')
    print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')
    return torre


def liberar_vaga(sistema):
    if sistema.vagas_ocupadas.tamanho <= 0:
        print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')
        print('Sem vagas ocupadas!')
        print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')
        return

    print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('Primeiro identifique a torre!')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')
    print('Lista de torres:\n')
    for torre in torres:
        print(torre)
    escolha = int(input('Digite o ID da torre: '))
    torre = next((torre for torre in torres if torre.id == escolha), None)
    i = 0

    if not torre:
        print('Torre não encontrada!')
        return

    print('Lista de apartamentos:\n')
    apartamentos_com_vaga = [apartamento for apartamento in torre.apartamentos if apartamento.vaga is not None]

    if not apartamentos_com_vaga:
        print('Nenhuma vaga ocupada nesta torre!')
        return

    for apartamento in apartamentos_com_vaga:
        print(apartamento)

    escolha = int(input('Digite o ID do apartamento para liberar a vaga:\n'))
    apartamento = next((apartamento for apartamento in torre.apartamentos if apartamento.id == escolha), None)

    if not apartamento or apartamento.vaga is None:
        print('Apartamento não encontrado ou já sem vaga!')
        return

    sistema.vagas_ocupadas.tamanho -= 1
    if sistema.fila_de_espera.inicio:
        sistema.fila_de_espera.inicio.vaga = apartamento.vaga
        apartamento.vaga = None
        sistema.fila_de_espera.adicionar = apartamento
    else:
        apartamento.vaga = None

    print('Vaga liberada!\n')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')


def mostrar_vagas(sistema):
    print('Apartamentos com vagas: \n')
    sistema.vagas_ocupadas.imprimir()
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')


def lista_espera(sistema):
    sistema.fila_de_espera.imprimir()
