import requests
import time
from config import API_URL, API_PARAMS
from logger import logger


MAX_RETRIES = 3
RETRY_DELAY = 5


def extract_crypto_data():

    for attempt in range(1, MAX_RETRIES + 1):

        try:

            logger.info(f"Requesting data from API (attempt {attempt})")

            response = requests.get(
                API_URL,
                params=API_PARAMS,
                timeout=10
            )

            response.raise_for_status()

            data = response.json()

            logger.info("Data successfully extracted from API")

            return data

        except requests.exceptions.RequestException as e:

            logger.error(f"API request failed: {e}")

            if attempt < MAX_RETRIES:

                logger.info(f"Retrying in {RETRY_DELAY} seconds...")
                time.sleep(RETRY_DELAY)

            else:

                logger.error("Max retries reached. Pipeline will stop.")
                raise