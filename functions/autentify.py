from functions.X import clear, reiniciar, menu2
from functions.config import *




_conta_atual = None
@property
def conta_atual(self):
    return self._conta_atual
    
@conta_atual.setter
def conta_atual(self, conta):
    if conta:
        self._conta_atual = conta  
    else:
        print('Conta não autenticada. Por favor, faça a autenticação primeiro.')

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
                clear()
                menu2()
                return True
            else:
                print('Autenticação não realizada, verifique os dados e tente novamente')
            return reiniciar()
        except Exception as e:
            print(f"Erro ao autenticar: {e}")