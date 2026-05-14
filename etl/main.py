from etl.extract.extract_csv import extract_csv
from etl.transform.transform_claims import (
    transform_claims
)
from etl.validate.validate_claims import (
    validate_claims
)
from etl.load.load_postgres import (
    load_to_postgres
)
from etl.utils.logger import logger


def run_claims_pipeline():

    logger.info(
        "Starting claims ETL pipeline"
    )

    # ==========================================
    # EXTRACT
    # ==========================================

    claims_df = extract_csv(
        "data/raw/claims.csv"
    )

    # ==========================================
    # TRANSFORM
    # ==========================================

    claims_df = transform_claims(
        claims_df
    )

    # ==========================================
    # VALIDATE
    # ==========================================

    validate_claims(claims_df)

    # ==========================================
    # LOAD
    # ==========================================

    load_to_postgres(
        claims_df,
        "claims_raw"
    )

    logger.info(
        "Claims ETL pipeline completed"
    )


if __name__ == "__main__":
    run_claims_pipeline()