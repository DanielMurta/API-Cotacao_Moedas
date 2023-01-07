# Importação do módulo request para enviar um pedido para a API
import requests
# Importação do módulo json p/ transformar a response da API em formato Json
import json
# Importação do módulo para criar a Interface gráfica
import PySimpleGUI as sg

# Definindo o tema da interface
sg.theme('DarkBlue')

# Definindo o formato do Layout da Interface 
layout = [
    [sg.Text('Cotação de moedas', font='arial 18')],
    [sg.Button('Dollar', font='arial 15'), sg.Button('Euro', font='arial 15'), sg.Button('Bitcoin', font='arial 15')],
    [sg.Text('', key='msg', font='arial 18')]
]

# Definindo o nome e as dimensões da janela
window = sg.Window('Cotação de Moedas', layout=layout, size=(350,150), element_justification='Center')

# Chamando o interface
while True:
    evento, valores = window.read()
    # Evento responsável por fechar a interface
    if evento == sg.WIN_CLOSED:
        exit()
    # Fazendo um pedido a API e colocando em uma variável    
    cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    # Tranformando a response para o formato Json
    cotacoes = cotacoes.json()
    # Para cada botão correspondente a moeda, o valor será exibido na interface.
    if evento == 'Dollar':
        cotacao_dolar = float(cotacoes['USDBRL']['bid'])
        window['msg'].update(f'R${cotacao_dolar:.2f}')
    elif evento == 'Euro':
        cotacao_euro = float(cotacoes['EURBRL']['bid'])
        window['msg'].update(f'R${cotacao_euro:.2f}')
    elif evento == 'Bitcoin':
        cotacao_bitcoin = float(cotacoes['BTCBRL']['bid'])
        window['msg'].update(f'R${cotacao_bitcoin:.2f}')




