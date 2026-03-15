from pathlib import Path


# =========================
# PATHS
# =========================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
LOG_DIR = BASE_DIR / "logs"


# =========================
# API CONFIG
# =========================

API_URL = "https://api.coingecko.com/api/v3/coins/markets"

API_PARAMS = {
    "vs_currency": "usd",
    "per_page": 100
}


# =========================
# COINS MONITORED
# =========================

TOP_COINS = [
    "bitcoin",
    "ethereum",
    "tether",
    "bnb",
    "solana"
]


# =========================
# FILES
# =========================

CRYPTO_DATA_FILE = DATA_DIR / "crypto_prices.csv"

CRYPTO_PIVOT_FILE = DATA_DIR / "crypto_prices_pivot.csv"