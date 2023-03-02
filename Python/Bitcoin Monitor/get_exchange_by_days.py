import requests
import json
from urllib import response
import conv_date

def get_currency_exchange(mainWindow, currency_code, num_days):
    url_currency_brl = f"http://economia.awesomeapi.com.br/json/daily/{currency_code}-BRL/{num_days}"
    response = requests.get(url_currency_brl)
    response_json = (response.json())

    for response_item in range(num_days):

        try:
        
            mainWindow.insert_text("-----------| BRL ---> {} |------------\n".format(currency_code))
            mainWindow.insert_text("Compra: _____________________ {}\n".format(str(response_json[response_item].get('bid'))))
            mainWindow.insert_text("Venda: ______________________ {}\n".format(str(response_json[response_item].get('ask'))))
            mainWindow.insert_text("Variação: ___________________ {}\n".format(str(response_json[response_item].get('varBid'))))
            mainWindow.insert_text("Variação (%): _______________ {}\n".format(str(response_json[response_item].get('pctChange'))))
            mainWindow.insert_text("Máximo: _____________________ {}\n".format(str(response_json[response_item].get('high'))))
            mainWindow.insert_text("Mínimo: _____________________ {}\n".format(str(response_json[response_item].get('low'))))
            mainWindow.insert_text("-----| Date: {} |-----\n\n".format(conv_date.conv_timestamp_to_date(int(response_json[response_item].get('timestamp')))))

        except:
            print("Erro genérico")
    

# get_currency_exchange()
#    Legendas
# timestamp   Data em formato timestamp
# bid         Compra
# ask         Venda
# varBid      Variação
# pctChange   Porcentagem de Variação
# high        Máximo
# low         Mínimo