import pandas as pd
from config import DATA_DIR, CRYPTO_DATA_FILE, CRYPTO_PIVOT_FILE

# garantir que pasta data existe
DATA_DIR.mkdir(exist_ok=True)


def load_data(df):

    if CRYPTO_DATA_FILE.exists():
        df.to_csv(CRYPTO_DATA_FILE, mode="a", header=False, index=False)
    else:
        df.to_csv(CRYPTO_DATA_FILE, index=False)


def create_pivot_table():

    df = pd.read_csv(CRYPTO_DATA_FILE)

    df["collected_at"] = pd.to_datetime(df["collected_at"])

    pivot = df.pivot_table(
        index="collected_at",
        columns="name",
        values="current_price"
    )

    pivot = pivot.sort_index()
    pivot = pivot.round(2)

    pivot = pivot.reset_index()

    pivot = pivot.rename(columns={"collected_at": "timestamp"})

    pivot["timestamp"] = pd.to_datetime(pivot["timestamp"]).dt.strftime("%Y-%m-%d %H:%M")

    pivot.to_csv(CRYPTO_PIVOT_FILE, index=False)

    create_excel_report(pivot)


def create_excel_report(pivot):

    excel_path = DATA_DIR / "crypto_prices_report.xlsx"

    with pd.ExcelWriter(excel_path, engine="xlsxwriter") as writer:

        pivot.to_excel(writer, sheet_name="Crypto Prices", index=False)

        workbook = writer.book
        worksheet = writer.sheets["Crypto Prices"]

        header_format = workbook.add_format({
            "bold": True,
            "bg_color": "#1f4e78",
            "font_color": "white",
            "border": 1
        })

        for col_num, value in enumerate(pivot.columns):
            worksheet.write(0, col_num, value, header_format)

        worksheet.set_column(0, 0, 20)
        worksheet.set_column(1, len(pivot.columns), 18)