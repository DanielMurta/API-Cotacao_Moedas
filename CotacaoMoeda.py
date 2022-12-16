import requests
import json
import PySimpleGUI as sg

sg.theme('DarkBlue')

layout = [
    [sg.Text('Cotação de moedas', font='arial 13')],
    [sg.Button('Dollar'), sg.Button('Euro'), sg.Button('Bitcoin')],
    [sg.Text('', key='msg')]
]

window = sg.Window('Cotação de Moedas', layout=layout, size=(300,100), element_justification='Center')

while True:
    evento, valores = window.read()
    if evento == sg.WIN_CLOSED:
        exit()
    cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    cotacoes = cotacoes.json()
    if evento == 'Dollar':
        cotacao_dolar = float(cotacoes['USDBRL']['bid'])
        window['msg'].update(f'R${cotacao_dolar:.2f}')
    elif evento == 'Euro':
        cotacao_euro = float(cotacoes['EURBRL']['bid'])
        window['msg'].update(f'R${cotacao_euro:.2f}')
    elif evento == 'Bitcoin':
        cotacao_bitcoin = float(cotacoes['BTCBRL']['bid'])
        window['msg'].update(f'R${cotacao_bitcoin:.2f}')




