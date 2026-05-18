import pandas as pd
from etl.validate.validate_claims import (
    validate_claims
)

def test_validate_claims():
    data = {

        "claim_id": [1],
        "claim_amount": [5000],
        "claim_status": ["OPEN"],
        "incident_type": ["COLLISION"],
        "claim_date": ["2025-01-01"],
        "fraud_flag": [False]
    }

    df = pd.DataFrame(data)
    result = validate_claims(df)

    assert result is True