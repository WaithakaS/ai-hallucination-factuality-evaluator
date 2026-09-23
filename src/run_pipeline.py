from pathlib import Path
from .evaluate import run
from .report import generate_report

ROOT=Path(__file__).resolve().parents[1]
INPUT=ROOT/"data/raw/factuality_benchmark.csv"
OUTPUT=ROOT/"data/processed/factuality_results.csv"
REPORT=ROOT/"reports/factuality_report.md"

if __name__=="__main__":
    df=run(INPUT,OUTPUT)
    generate_report(OUTPUT,REPORT)
    print(df[["example_id","label","support_score","contradiction_signal"]].to_string(index=False))
