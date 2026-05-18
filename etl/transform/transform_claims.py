import pandas as pd
from etl.utils.logger import logger

def transform_claims(df):
    logger.info(
        "Starting claims transformation"
    )

    # ==========================
    # Lowercase columns
    # ==========================

    df.columns = (
        df.columns
        .str.lower()
    )

    # ==========================
    # Remove duplicates
    # ==========================

    initial_rows = len(df)

    df.drop_duplicates(inplace=True)
    logger.info(
        f"Duplicates removed: "
        f"{initial_rows - len(df)}"
    )

    # ==========================
    # Remove invalid amounts
    # ==========================

    df = df[df["claim_amount"] > 0]

    # ==========================
    # Normalize status
    # ==========================

    df["claim_status"] = (
        df["claim_status"]
        .str.upper()
    )
    df["incident_type"] = (
        df["incident_type"]
        .str.upper()
    )

    # ==========================
    # Convert claim_date
    # ==========================

    df["claim_date"] = (
        df["claim_date"]
        .astype("datetime64[ns]")
    )

    # ==========================
    # Add processing timestamp
    # ==========================

    df["etl_processed_date"] = (
        pd.Timestamp.now()
    )
    logger.info(
        "Claims transformation completed"
    )
    return df