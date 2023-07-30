
from functions.X import sleep, clear, reiniciar
from functions.registerDelete import cadastro, excluir, accountList
from functions.autentify import autenticar
from functions.config import sys



def menu():
    print('Bem vindo ao banco dos programadores')
    sleep(1)
    start = input('Você ja tem uma conta?\n (1)Sim \n (2)Não\n (3)Excluir conta:\n (4)Listar contas:\n (5)Sair\n')
    if start == '1':
        nome = input('Digite seu nome: ')
        agencia = input('Digite sua agência: ')
        conta = input('Digite sua conta: ')
        print('Autenticando...')
        sleep(2)
        autenticar(conta, nome, agencia) # type: ignore
    elif start == '2':
        resp1 = input('Goataria de criar uma conta? \n (1)Sim \n (2)Não\n')
        if resp1 == '1':
            cadastro()
            sleep(2)   
            clear()
            reiniciar()
        elif resp1 == '2':
            print('Ok, vamos voltar ao menu...')
            reiniciar()                    

    elif start == '3':
        excluir()                     

    elif start == '4':
        accountList()          

    elif start == '5':
        print('Saindo...')
        sleep(2)
        sys.exit()
            
    else:
        print('Opção inválida')
        sleep(2)
        reiniciar() 
    return True  