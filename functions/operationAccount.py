from functions.config import *

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