#Importação das bibliotecas
from tkinter.constants import FALSE, TRUE
from PySimpleGUI.PySimpleGUI import WINDOW_CLOSED, Window
import layout
import script
import ArqTXT

# Utilização das senhas geradas anteriormente(ERRADO)
tipo=layout.senhasanteriores()
if tipo == 'NAO':
    ArqTXT.CriarArquivo()
while TRUE:
    tipo = layout.TelaPrincipal() # Tela principal do programa
    if tipo == WINDOW_CLOSED:
        break
    else:
        setor=layout.tipoCaixa() # Escolher o tipo do atendimento
        if setor != 'VOLTAR':
            script.Ticket(tipo,setor)