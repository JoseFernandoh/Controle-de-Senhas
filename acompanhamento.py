# Importação das bibliotecas
from tkinter.constants import TRUE
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import WINDOW_CLOSED
import ArqTXT
import layout
import script


# Tela de acompanhamento das senhas
senha=['CXC(Sem Senha)','CXP(Sem Senha)','GHC(Sem Senha)','GHP(Sem Senha)','GEC(Sem Senha)','GEP(Sem Senha)']
bancada=['000','000','000','000','000','000']
while TRUE:
    tipo = layout.acompanhamento(senha,bancada)
    if tipo == WINDOW_CLOSED:
        break
    else:
        senha[int(tipo[3])]= ArqTXT.PegarSenhaAcompanhamento(tipo)
        bancada[int(tipo[3])] = script.caixa_mesa()
        if senha[int(tipo[3])] == '':
            senha[int(tipo[3])]=str(tipo[0:3])+'(Sem Senha)'
            bancada[int(tipo[3])]='000'
        

