import pandas as pd
from datetime import datetime


def transform_crypto_data(data):

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

    return df