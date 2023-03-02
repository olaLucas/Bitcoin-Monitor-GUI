import requests
import json
from urllib import response

def get_currency_exchange(mainWindow, currency_code):
    url_currency_brl = f"http://economia.awesomeapi.com.br/json/last/{currency_code}-BRL"

    response = requests.get(url_currency_brl)
    response_json = (response.json()['BTCBRL'])

    try:
        
        mainWindow.insert_text("---------| BRL ---> {} |---------\n".format(currency_code))
        mainWindow.insert_text("Compra: _____________________ {}\n".format(str(response_json.get('bid'))))
        mainWindow.insert_text("Venda: ______________________ {}\n".format(str(response_json.get('ask'))))
        mainWindow.insert_text("Variação: ___________________ {}\n".format(str(response_json.get('varBid'))))
        mainWindow.insert_text("Variação (%): _______________ {}\n".format(str(response_json.get('pctChange'))))
        mainWindow.insert_text("Máximo: _____________________ {}\n".format(str(response_json.get('high'))))
        mainWindow.insert_text("Mínimo: _____________________ {}\n".format(str(response_json.get('low'))))
        
    except:
        print("Erro genérico")

#    Legendas
# key         Label
# bid         Compra
# ask         Venda
# varBid      Variação
# pctChange   Porcentagem de Variação
# high        Máximo
# low         Mínimo
