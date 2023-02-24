import requests
import json
from urllib import response


def get_currency_exchange(currency_code):
    # currency_code = "BTC"
    url_currency_brl = f"http://economia.awesomeapi.com.br/json/last/{currency_code}-BRL"

    response = requests.get(url_currency_brl)
    # print(url_currency_brl)

    # print(response)
    response_json = (response.json()['BTCBRL'])
    # print(response_json)
    try:
        print(f"Compra: BRL->{currency_code}: " + str(response_json.get('bid')))
        print(f"Venda: BRL->{currency_code}: " + str(response_json.get('ask')))
        print(f"Variação: BRL->{currency_code}: " + str(response_json.get('varBid')))
        print(f"Porcentagem de Variação: BRL->{currency_code}: " + str(response_json.get('pctChange')))
        print(f"Máximo: BRL->{currency_code}: " + str(response_json.get('high')))
        print(f"Mínimo: BRL->{currency_code}: " + str(response_json.get('low')))
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
