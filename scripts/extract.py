import requests
from config import API_URL, API_PARAMS


def extract_crypto_data():

    response = requests.get(API_URL, params=API_PARAMS)

    data = response.json()

    return data