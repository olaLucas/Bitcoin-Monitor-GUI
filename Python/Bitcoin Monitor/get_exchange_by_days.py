import requests
import json
from urllib import response
import conv_date

def get_currency_exchange(currency_code, num_days):
    # currency_code = "BTC"
    # num_days = 5
    url_currency_brl = f"http://economia.awesomeapi.com.br/json/daily/{currency_code}-BRL/{num_days}"

    response = requests.get(url_currency_brl)
    # print(url_currency_brl)

    # print(response)
    response_json = (response.json())
    # print(response_json)

    for response_item in range(num_days):
        # print(response_item)
        try:
            print(f"Compra: BRL->{currency_code}: " + str(response_json[response_item].get('bid')))
            print(f"Venda: BRL->{currency_code}: " + str(response_json[response_item].get('ask')))
            print(f"Variação: BRL->{currency_code}: " + str(response_json[response_item].get('varBid')))
            print(f"Porcentagem de Variação: BRL->{currency_code}: " + str(response_json[response_item].get('pctChange')))
            print(f"Máximo: BRL->{currency_code}: " + str(response_json[response_item].get('high')))
            print(f"Mínimo: BRL->{currency_code}: " + str(response_json[response_item].get('low')))
            date = conv_date.conv_timestamp_to_date(int(response_json[response_item].get('timestamp')))
            print(f"Data: {date}")
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