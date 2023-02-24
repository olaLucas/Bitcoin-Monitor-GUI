print("E la vamos nós")

currency_option = int(input("Qual moeda deseja monitorar \n (1)BTC? "))
option = int(input(
    "Qual operação dejesa consultar? \n (1) Cotação Atual \n (2) Cotação por dias \n"))

currency_code = "BTC"

if(option == 1):
    import get_current_exchange
    ret = (get_current_exchange.get_currency_exchange(currency_code))
elif (option == 2):
    import get_exchange_by_days
    num_days = int(
        input("Entre com a quantidade de dias a serem consultados: "))
    ret = (get_exchange_by_days.get_currency_exchange(currency_code, num_days))
else:
    print("OPÇÃO INVÁLIDA")