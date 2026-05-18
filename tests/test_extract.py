import pandas as pd
from etl.extract.extract_csv import (
    extract_csv
)

def test_extract_csv():
    df = extract_csv(
        "data/raw/claims.csv"
    )

    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0