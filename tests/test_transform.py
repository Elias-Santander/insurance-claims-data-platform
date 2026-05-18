import pandas as pd
from etl.transform.transform_claims import (
    transform_claims
)

def test_transform_claims():
    data = {
        "claim_id": [1],
        "claim_amount": [5000],
        "claim_status": ["open"],
        "incident_type": ["collision"],
        "claim_date": ["2025-01-01"],
        "fraud_flag": [False]
    }

    df = pd.DataFrame(data)
    transformed_df = transform_claims(df)

    assert transformed_df.loc[0, "claim_status"] == "OPEN"
    assert transformed_df.loc[0, "incident_type"] == "COLLISION"
    assert pd.api.types.is_datetime64_any_dtype(
        transformed_df["claim_date"]
    )