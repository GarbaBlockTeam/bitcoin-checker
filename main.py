import requests

def get_bitcoin_price():
    # URL API для получения последней цены биткоина в USD
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        # Извлечение цены биткоина в USD
        price = data['bpi']['USD']['rate']
        print(f"Текущая стоимость биткоина: ${price}")
    except requests.exceptions.RequestException as e:
        print(e)

get_bitcoin_price()
