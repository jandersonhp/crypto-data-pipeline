import requests

def extract_crypto_data():

    url = "https://api.coingecko.com/api/v3/coins/markets"

    params = {
        "vs_currency": "usd"
    }

    response = requests.get(url, params=params)

    data = response.json()

    return data