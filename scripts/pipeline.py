from extract import extract_crypto_data
from transform import transform_crypto_data
from load import load_data
from logger import logger


def run_pipeline():

    logger.info("Starting crypto pipeline")

    data = extract_crypto_data()
    logger.info("Data extracted from API")

    df = transform_crypto_data(data)
    logger.info("Data transformed")

    load_data(df)
    logger.info("Data loaded to CSV")

    logger.info("Pipeline finished successfully")


if __name__ == "__main__":
    run_pipeline()