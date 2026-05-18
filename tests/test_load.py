import pandas as pd

def test_dataframe_creation():
    data = {
        "claim_id": [1],
        "claim_amount": [1000]
    }

    df = pd.DataFrame(data)
    
    assert len(df.columns) == 2