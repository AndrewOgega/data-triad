import logging

import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account
from pydantic_settings import BaseSettings

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class Settings(BaseSettings):
    BQ_KEY: str

    class Config:
        env_file = ".env"


def load_credit_data() -> pd.DataFrame:
    """
    Load credit card default data from BigQuery or local CSV file.

    Returns:
        pd.DataFrame: DataFrame containing the credit card default data.
    """
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )

    # TODO could have used a fucntion for this one.

    try:
        settings = Settings()

        credentials = service_account.Credentials.from_service_account_file(
            settings.BQ_KEY
        )

        client = bigquery.Client(
            credentials=credentials, project=credentials.project_id
        )

        logging.info("Attempting to load data from BigQuery...")

        df: pd.DataFrame = (
            client.query(
                "SELECT * FROM `bigquery-public-data.ml_datasets.credit_card_default`"
            )
            .to_dataframe()
            .set_index("id")
        )

        # could be problemtic for larger datasets
        df.to_csv("credit_card_default.csv", index="id")

        logging.info("Data successfully loaded from BigQuery and saved to CSV.")

    except Exception as e:
        logging.warning(f"Failed to load from BigQuery. Reason: {e}")
        logging.info("Loading data from local CSV instead...")

        df: pd.DataFrame = pd.read_csv("credit_card_default.csv").set_index("id")

    # TODO handle for missing .csv file

    return df
