"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.
Conta (ABC)
    ContaCorrente
    ContaPoupanca
Pessoa (ABC)
    Cliente
        Clente -> Conta
Banco
    Banco -> Cliente
    Banco -> Conta
Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""
from abc import ABC, abstractmethod
from time import sleep

import sqlite3
TABLE_NAME = 'CONTA'
conn = sqlite3.connect('db.banco')
cursor = conn.cursor()

class cadastramento(ABC):
    def __init__(self, nome=None, agencia=None, conta=None, saldo=0, limite=0):
        self._nome = nome
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo
        self._limite = limite
    
    def cadastro(self):
        while True:
            nome = input('Digite seu nome: ')
            if nome.strip().isalpha():
                self._nome = nome
                break
            else:
                print('Nome inválido. Digite apenas letras.')
        while True:
            agencia = input('Digite sua agência: ')
            if agencia.strip().isnumeric():
                self._agencia = agencia
                break
            else:
                print('Agência inválida. Digite apenas números.')
        while True:
            conta = input('Digite sua conta: ')
            if conta.strip().isnumeric():
                self._conta = conta
                break
            else:
                print('Conta inválida. Digite apenas números.')
        
        conn.execute('INSERT INTO CONTA (nome, agencia, conta, saldo, limite) VALUES (?, ?, ?, ?, ?)',
                     (self._nome, self._agencia, self._conta, self._saldo, self._limite))
        conn.commit()
        print('Cadastro realizado com sucesso.')  
        sleep(2)  
        print({'nome': self._nome, 'agencia': self._agencia, 'conta': self._conta})
cadastrar = []






