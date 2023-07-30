
from functions.config import *
from functions.menu import menu
from functions.operationAccount import *
from functions.autentify import *

def accountList():
    cursor.execute(f'SELECT * FROM {TABLE_NAME}')
    result = cursor.fetchall()
    clear()
    for register in result:
        _Aid = register[0]
        nome = register[1]
        agencia = register[2]
        conta = register[3]
        valor = register[4]
        print("=======================================")
        print("Nome:", nome)
        print("Agência:", agencia)
        print("Conta:", conta)
        print("Saldo:", valor)
        print("ID:", _Aid)
        print("=======================================")
        sleep(5)
        reiniciar()



def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def reiniciar():
    sleep(2)
    clear()
    menu()

    

def menu2():
    clear()
    while True:
        opcao = input('O que você deseja fazer?\n (1) Depositar\n (2) Sacar\n (3) Valor em conta\n (4) Sair:\n')

        if opcao == '1':
            clear()
            valor = float(input('Digite o valor que deseja depositar: '))
            print('Depositando...')
            sleep(2)  
            deposito(valor, _conta_atual) # type: ignore

        elif opcao == '2':
            valor = float(input('Digite o valor que deseja sacar: '))
            if conta_atual:
                saque(conta_atual, valor)
            else:
                print('Conta não autenticada. Por favor, faça a autenticação primeiro.')

        elif opcao == '3':
            saldo(self.conta_atual)
            

        elif opcao == '4':
            print('Saindo...')
            break

        else:
            print('Opção inválida. Por favor, escolha uma opção válida.')




def saldo( conta):
    conta = conta_atual
    try:
        cursor.execute(f"SELECT * FROM {TABLE_NAME} WHERE conta = ?", (conta,))
        result = cursor.fetchone()
        print('Consultando saldo...')
        sleep(2)
        clear()
        print('='*50)
        print(f"O saldo da conta {result[1]} é de R$ {result[4]}")
        print('='*50)
    except Exception as e:
     print(f"Erro ao consultar a tabela: {e}")
    return result[0] # type: ignore 