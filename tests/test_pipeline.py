import pandas as pd
from src.evaluate import run

def test_pipeline(tmp_path):
    source=tmp_path/"input.csv"; output=tmp_path/"results.csv"
    pd.DataFrame([{"example_id":"T1","question":"Capital?","reference_answer":"Paris is the capital of France.","model_answer":"Paris is the capital of France.","category":"geography"}]).to_csv(source,index=False)
    result=run(source,output)
    assert len(result)==1 and output.exists()
