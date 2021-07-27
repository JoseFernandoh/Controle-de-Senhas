from tkinter.constants import FALSE
import PySimpleGUI as sg

def senhasanteriores(): # Tela de senhas anteriores
    layout =[
        [sg.T(' '* 20),sg.Text('SISTEMA DO BANCO DO BRASIL', justification='center', size=(40,2))],
        [sg.T(' '* 20),sg.Text('Deseja Usar As Senhas Anteriores', justification='center', size=(40,4))],
        [sg.RealtimeButton('SIM' ,size=(20,4)),sg.T(' '  * 35), sg.RealtimeButton('NAO',size=(20,4))]
    ]
    WINDOW = sg.Window("Senhas Anteriores").layout(layout)
    event,values = WINDOW.Read()
    tipo = event
    WINDOW.close()
    return tipo

def acompanhamento(senha,bancada): # Telas de acompnhamento das senhas
    layout = [
        [sg.Text('Acompanhamento de Senhas',size=(0,2))],
        [sg.Text('Senha',size=(15,1)),sg.Text('Caixa/Mesa')],
        [sg. Text(senha[0],size=(17,1)),sg.Text(bancada[0]),sg.T(' '*3),sg.Button('Proximo', key='CXC0')],
        [sg. Text(senha[1],size=(17,1)),sg.Text(bancada[1]),sg.T(' '*3),sg.Button('Proximo', key='CXP1')],
        [sg. Text(senha[2],size=(17,1)),sg.Text(bancada[2]),sg.T(' '*3),sg.Button('Proximo', key='GHC2')],
        [sg. Text(senha[3],size=(17,1)),sg.Text(bancada[3]),sg.T(' '*3),sg.Button('Proximo', key='GHP3')],
        [sg. Text(senha[4],size=(17,1)),sg.Text(bancada[4]),sg.T(' '*3),sg.Button('Proximo', key='GEC4')],
        [sg. Text(senha[5],size=(17,1)),sg.Text(bancada[5]),sg.T(' '*3),sg.Button('Proximo', key='GEP5')],
        ]
    WINDOW = sg.Window("Dados Do Usuario").layout(layout)
    event,values = WINDOW.Read()
    WINDOW.close()
    return event

def TelaPrincipal(): # Tela Do tipo de Atendimento

    layout =[
        [sg.T(' '* 20),sg.Text('SISTEMA DO BANCO DO BRASIL', justification='center', size=(40,2))],
        [sg.T(' '* 20),sg.Text('Informe O Tipo De Atendimento', justification='center', size=(40,4))],
        [sg.RealtimeButton('Convencional' ,key='C',size=(20,4)),sg.T(' '  * 35), sg.RealtimeButton('Preferencial' ,key='P',size=(20,4))]
    ]

    WINDOW = sg.Window("Dados Do Usuario").layout(layout)
    event,values = WINDOW.Read()
    tipo = event
    WINDOW.close()
    return tipo

def tipoCaixa(): # Tela de seleção do Setor de Atendimento
    layout =[
        [sg.T(' '* 20),sg.Text('INFORME O SETOR DE ATENDIMENTO',justification='center',size=(0,3))],
        [sg.Button('CAIXA',key='CX',size=(20,3)),sg.T(' '* 20),sg.Button('GUICHE',key='GH',size=(20,3))],
        [sg.Text(size=(20,1))],
        [sg.Button('GERENCIA',key='GE',size=(20,3)),sg.T(' ' * 20),sg.Button('VOLTAR',size=(20,3))]
        

    ]
    WINDOW = sg.Window("BANCO DO BRASIL").layout(layout)
    event,values = WINDOW.Read()
    tipo = event
    WINDOW.close()
    return tipo
