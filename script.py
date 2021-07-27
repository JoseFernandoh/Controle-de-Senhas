# Importação das bibliotecas
from datetime import datetime
import ArqTXT
import random


def Gerarsenha(tipo, setor): # Gerador de senhas
    cont = ArqTXT.PegarSenha(tipo,setor)
    senha = setor+tipo+f"{cont+1:03}"
    return senha

def caixa_mesa(): # seleção do caixa ou mesa
    bancada=f"{random.randint(1,10):03}"
    return bancada
    
def Ticket(tipo, setor): # Gerador de ticket

# Atulizador de data e hora do ticket
    data = datetime.now()
    data = data.strftime('%d/%m/%Y')
    hora = datetime.now()
    hora = hora.strftime('%H:%M')

    senha=Gerarsenha(tipo , setor)
    ArqTXT.SalvarSenha(senha)
# Tipo de Atendimento
    if tipo =='C':
        ent='Convencional'
    else:
        ent='Preferencial'
    if setor[0]=='G':
        bancada = 'MESA'
    else:
        bancada = 'CAIXA'
# Ticket printado na tela com as informações do atendimento do cliente
    print('========================================\n')
    print('       SISTEMA DE GESTAO DE FILAS       \n')
    print('========================================\n')
    print('           BANCO DO BRASIL              \n')
    print('      Av. Principal Nº 100, Centro      \n')
    print('          Fone(99)-9-9199-1907          \n')
    print('----------------------------------------\n')
    print('             SENHA:'+senha+'               \n')
    print('           CAIXA/MESA:'+bancada+'             \n')
    print('           Tipo: '+ent,'           \n')
    print('            Data '+data+'             \n')
    print('           Hora '+hora+' horas             \n')
    print('========================================\n')

