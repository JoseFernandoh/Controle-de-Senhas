from tkinter.constants import TRUE
local = 'Senhas/Senha.txt'

def CriarArquivo(): # Criando arquivos txt para guardar as senhas
    arquivo = open(local, 'w')


def SalvarSenha(senha): # Salvar as senhas em um arquivo txt
    arquivo = open(local, 'r')
    conteudo = arquivo.readlines()
    conteudo.append(str(senha)+"\n")

    arquivo = open(local, 'w')
    arquivo.writelines(conteudo)

    arquivo.close()

def PegarSenhaAcompanhamento(tipo):    
    conteudo=[]    
    arquivo = open(local, 'r')

    while TRUE:
        senha = arquivo.readline()
        if senha[0:3]==tipo[0:3]:
            break
        if senha == '':
            break
        conteudo.append(senha)

    conteudorest = arquivo.readlines()
    arquivo = open(local, 'w')
    arquivo.writelines(conteudo+conteudorest)
    arquivo.close
    return senha



def PegarSenha(tipo, setor):     
    cont=0
    arquivo = open(local, 'r')
    while TRUE:
        senha = arquivo.readline()
        if senha[0:3]==setor+tipo:
            cont=cont+1
        if senha == '':
            break
    arquivo.close
    return cont
    
    
    

