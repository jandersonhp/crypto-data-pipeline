from extract import extract_crypto_data
from transform import transform_crypto_data
from load import load_data


def run_pipeline():

    data = extract_crypto_data()

    df = transform_crypto_data(data)

    load_data(df)

    print("Pipeline executado com sucesso!")


if __name__ == "__main__":
    run_pipeline()