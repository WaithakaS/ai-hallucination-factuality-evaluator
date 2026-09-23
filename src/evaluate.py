from pathlib import Path
import pandas as pd
from .factuality import evaluate_dataset

def run(input_path, output_path):
    df = pd.read_csv(input_path)
    result = pd.concat([df, pd.DataFrame(evaluate_dataset(df))], axis=1)
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    result.to_csv(output_path, index=False)
    return result
