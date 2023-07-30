from functions.config import * 
from functions.X import *
TABLE_NAME = 'CONTA'
conn = sqlite3.connect('db.banco')
cursor = conn.cursor()

#dentro de um DEF?
_nome = nome = None
_agencia = agencia = None
_conta = conta = None
_saldo = saldo = 0
_limite = limite = 0

def cadastro():
    while True:
        nome = input('Digite seu nome: ')
        if nome.strip().isalpha():
            _nome = nome
            break
        else:
            print('Nome inválido. Digite apenas letras.')
    while True:
        agencia = input('Digite sua agência: ')
        if agencia.strip().isnumeric():
            _agencia = agencia
            break
        else:
            print('Agência inválida. Digite apenas números.')
    while True:
        conta = input('Digite sua conta: ')
        if conta.strip().isnumeric():
            _conta = conta
            break
        else:
            print('Conta inválida. Digite apenas números.')
    
    conn.execute('INSERT INTO CONTA (nome, agencia, conta, saldo, limite) VALUES (?, ?, ?, ?, ?)', (_nome, _agencia, _conta, _saldo, _limite))
    conn.commit()
    print('Cadastro realizado com sucesso.')  
    sleep(2)  
    print({'nome': _nome, 'agencia': _agencia, 'conta': _conta})
cadastrar = [] 

def excluir(conta=None):
    while True:
        conta = input('Digite a conta que quer excluir: | Ou digite Sir para voltar ao menu ')
        if conta == 'Sair':
            print('Voltando ao menu...')
            sleep(2)
            reiniciar()
            break
        if conta.isdigit():
            try:
                cursor.execute(f"SELECT conta FROM {TABLE_NAME} WHERE conta = ?", (conta,))
                result = cursor.fetchone()
                print("Procurando conta...")
                print(result[0])
                print(conta)
                sleep(2)
                if result is not None and conta == result[0]:
                    print('Conta encontrada.')
                    sleep(2)
                    cursor.execute(f"DELETE FROM {TABLE_NAME} WHERE conta = ?", (conta))
                    conn.commit()
                    print('Conta excluída com sucesso.')
                    sleep(2)
                    reiniciar()
                    break
                else:
                    if result is None:
                        print('Conta não encontrada.')
                        sleep(2)
                    else:
                        print('Conta não encontrada.')
                        sleep(2)
                        reiniciar()
            except Exception as e:
                print('Erro ao excluir conta: ', e)
                sleep(5)
                
        elif conta == 'Sair':
            print('Voltando ao menu...')
            sleep(2)
            reiniciar()
            break
        else:  
            print('Conta inválida, digite o número da conta!, ou digite "Sair" para voltar ao menu')
            sleep(2)
