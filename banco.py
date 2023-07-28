# """
# Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
# Criar um sistema bancário (extremamente simples) que tem clientes, contas e
# um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
# possa sacar/depositar nessa conta. Contas corrente tem um limite extra.
# Conta (ABC)
#     ContaCorrente
#     ContaPoupanca
# Pessoa (ABC)
#     Cliente
#         Clente -> Conta
# Banco
#     Banco -> Cliente
#     Banco -> Conta
# Dicas:
# Criar classe Cliente que herda da classe Pessoa (Herança)
#     Pessoa tem nome e idade (com getters)
#     Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
# Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
#     ContaCorrente deve ter um limite extra
#     Contas têm agência, número da conta e saldo
#     Contas devem ter método para depósito
#     Conta (super classe) deve ter o método sacar abstrato (Abstração e
#     polimorfismo - as subclasses que implementam o método sacar)
# Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
# Banco será responsável autenticar o cliente e as contas da seguinte maneira:
#     Banco tem contas e clentes (Agregação)
#     * Checar se a agência é daquele banco
#     * Checar se o cliente é daquele banco
#     * Checar se a conta é daquele banco
# Só será possível sacar se passar na autenticação do banco (descrita acima)
# Banco autentica por um método.

import sqlite3
from cadastroCliente import cadastramento
from time import sleep
import os
import sys
TABLE_NAME = 'CONTA' 
conn = sqlite3.connect('db.banco')
cursor = conn.cursor()

cadastrar = cadastramento()
          



# class Banco:
#     def __init__(self, nome, agencia, conta):
#         self.nome = nome
#         self.agencia = agencia
#         self.conta = conta
# from cadastroCliente import *
# class contaConrrente(ABC):
#     def __init__(self, saldo, limite, agencia, conta):
#         self.saldo = saldo
#         self.limite = limite
#         self.agencia = agencia
#         self.conta = conta
        
class Operacoes():
    def __init__(self):
       self._conta_atual = None
       self.menu()
        

    @property
    def conta_atual(self):
       return self._conta_atual
    
    @conta_atual.setter
    def conta_atual(self, conta):
       if conta:
           self._conta_atual = conta  
       else:
           print('Conta não autenticada. Por favor, faça a autenticação primeiro.')
     
    def listen(self):
        cursor.execute(f'SELECT * FROM {TABLE_NAME}')
        result = cursor.fetchall()
        self.clear()
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
        self.reiniciar()
   
    def autenticar(self, nome, agencia, conta):
       with sqlite3.connect('db.banco') as conn:
           cursor = conn.cursor()
           cursor.execute(f"SELECT nome, agencia, conta FROM {TABLE_NAME} WHERE nome=? AND agencia=? AND conta=?", (nome, agencia, conta))
           result = cursor.fetchone()
           print(result)
           try:
               if result:
                   self.conta_atual = conta
                   sleep(2)
                   print('Autenticação realizada com sucesso')
                   sleep(2)
                   self.clear()
                   self.menu2()
                   return True
               else:
                   print('Autenticação não realizada, verifique os dados e tente novamente')
               return self.reiniciar()
           except Exception as e:
              print(f"Erro ao autenticar: {e}")
    
    def clear(self):
       os.system('cls' if os.name == 'nt' else 'clear')
     
    def reiniciar(self):
        sleep(2)
        self.clear()
        self.menu()

    def menu(self):
        print('Bem vindo ao banco dos programadores')
        sleep(1)
        comeco2 = input('Você ja tem uma conta?\n (1)Sim \n (2)Não\n (3)Excluir conta:\n (4)Listar contas:\n (5)Sair\n')
        if comeco2 == '1':
            nome = input('Digite seu nome: ')
            agencia = input('Digite sua agência: ')
            conta = input('Digite sua conta: ')
            print('Autenticando...')
            sleep(2)
            self.autenticar(nome, agencia, conta)

        elif comeco2 == '2':
            resp1 = input('Goataria de criar uma conta? \n (1)Sim \n (2)Não\n')
            if resp1 == '1':
                cadastramento().cadastro()
                sleep(2)   
                self.clear()
                self.reiniciar()
            elif resp1 == '2':
                print('Ok, vamos voltar ao menu...')
                self.reiniciar()                    

        elif comeco2 == '3':
            self.excluir()                     

        elif comeco2 == '4':
            self.listen()          

        elif comeco2 == '5':
            print('Saindo...')
            sleep(2)
            sys.exit()
             
        else:
            print('Opção inválida')
            sleep(2)
            self.reiniciar() 
        return True   

    def menu2(self):
     self.clear()
     while True:
       opcao = input('O que você deseja fazer?\n (1) Depositar\n (2) Sacar\n (3) Valor em conta\n (4) Sair:\n')

       if opcao == '1':
           self.clear()
           valor = float(input('Digite o valor que deseja depositar: '))
           print('Depositando...')
           sleep(2)  
           self.deposito(valor, self._conta_atual)

       elif opcao == '2':
           valor = float(input('Digite o valor que deseja sacar: '))
           if self._conta_atual:
               self.saque(valor, self._conta_atual)
           else:
               print('Conta não autenticada. Por favor, faça a autenticação primeiro.')

       elif opcao == '3':
           self.saldo(self._conta_atual)
           

       elif opcao == '4':
           print('Saindo...')
           break

       else:
           print('Opção inválida. Por favor, escolha uma opção válida.')


    def excluir(self, conta=None):
       while True:
        conta = input('Digite a conta que quer excluir: | Ou digite Sir para voltar ao menu ')
        if conta == 'Sair':
            print('Voltando ao menu...')
            sleep(2)
            self.reiniciar()
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
                    self.reiniciar()
                    break
                else:
                    if result is None:
                        print('Conta não encontrada.')
                        sleep(2)
                    else:
                        print('Conta não encontrada.')
                        sleep(2)
                        self.reiniciar()
            except Exception as e:
                print('Erro ao excluir conta: ', e)
                sleep(5)
                
        elif conta == 'Sair':
            print('Voltando ao menu...')
            sleep(2)
            self.reiniciar()
            break
        else:  
            print('Conta inválida, digite o número da conta!, ou digite "Sair" para voltar ao menu')
            sleep(2)
    
    def deposito(self, valor, conta):
        conta = self._conta_atual
        valor = float(valor)
        try:          
            # Verificar se o saldo é NULL
            cursor.execute(f"SELECT saldo FROM {TABLE_NAME} WHERE conta = ?", (conta,))
            result = cursor.fetchone()
            try:
                if result is None or result[0] is None:
                    # Inserir um registro com o saldo inicial
                    cursor.execute(f"INSERT INTO {TABLE_NAME} (conta, saldo) VALUES (?, 0)", (conta,))
                    conn.commit()
            except Exception as e:
                print(f"Erro ao inserir um registro: {e}")
            # Atualizar o saldo com o valor do depósito
            cursor.execute(f"UPDATE {TABLE_NAME} SET saldo = saldo + ? WHERE conta = ?", (valor, conta,))
            conn.commit()
            
            
            print('Depósito realizado com sucesso')
            sleep(2)
            self.clear()
            self.menu2()
            
        except Exception as e:
            print(f"Erro ao atualizar a tabela: {e}")
            return valor
        
    def saque(self, valor, conta):
        conta = self._conta_atual
        valor = float(valor)
        try:
            # Verificar se o saldo é NULL
            cursor.execute(f"SELECT saldo FROM {TABLE_NAME} WHERE conta = ?", (conta,))
            result = cursor.fetchone()
            if result is None or result == 0:
                print('Consultando saldo...')
                sleep(2)
                print('Não há saldo para sacar')
                sleep(2)   
                self.clear()
                self.menu2()
                return
            elif result[0] < valor:
                print('Consultando saldo...')
                sleep(2)
                print('Saldo insuficiente')
                sleep(2)
                self.clear()
                self.menu2()
                return
            else:
            # Atualizar o saldo com o valor do depósito
                cursor.execute(f"UPDATE {TABLE_NAME} SET saldo = saldo - ? WHERE conta = ?", (valor, conta,))
                conn.commit()
            
            print('Consultando saldo...')
            sleep(2)
            print('conferindo valor...')
            sleep(2)
            print('Saque realizado com sucesso')
            sleep(2)
            self.clear()
            self.menu2()
        except Exception as e:
            print(f"Erro ao atualizar a tabela: {e}")
        return valor

    def saldo(self, conta):
       conta = self._conta_atual
       try:
        cursor.execute(f"SELECT * FROM {TABLE_NAME} WHERE conta = ?", (conta,))
        result = cursor.fetchone()
        print('Consultando saldo...')
        sleep(2)
        self.clear()
        print('='*50)
        print(f"O saldo da conta {result[1]} é de R$ {result[4]}")
        print('='*50)
       except Exception as e:
           print(f"Erro ao consultar a tabela: {e}")
       return result[0] # type: ignore 

if __name__ == '__main__':
    Operacoes()
    