import pandas as pd
from datetime import datetime


TOP_COINS = [
    "bitcoin",
    "ethereum",
    "tether",
    "bnb",
    "solana"
]


def transform_crypto_data(data):

    df = pd.DataFrame(data)

    # filtrar moedas principais
    df = df[df["id"].isin(TOP_COINS)]

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

    return df