from pathlib import Path
from datetime import datetime
import requests
import pandas as pd

##caminhos aboslutos com pathlib
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

#api coingecko
url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd"
}

response = requests.get(url, params=params)

data = response.json()

#dataframe
df = pd.DataFrame(data)
df["collected_at"] = datetime.now()

df = df[
    [
        "name",
        "symbol",
        "current_price",
        "market_cap",
        "total_volume",
        "collected_at"
    ]
]

print(df.head())

df.to_csv(DATA_DIR / "crypto_prices.csv", index=False)