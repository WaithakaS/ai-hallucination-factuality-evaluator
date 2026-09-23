# AI Hallucination & Factuality Evaluator

A transparent baseline tool for screening AI-generated answers against trusted reference answers and identifying **potentially unsupported or contradictory claims**.

> **Important:** This project does not determine truth automatically. It uses lightweight text-based signals for evaluation research and human-review triage.

## Features
- Text normalisation
- Lexical overlap
- Sequence similarity
- Numeric contradiction signal
- Transparent support score
- Batch CSV evaluation
- Markdown report
- Streamlit interface
- Pytest test suite
- Synthetic benchmark

## Methodology

```text
Reference Answer + AI Answer
            ↓
   Normalisation
            ↓
 Similarity + Overlap
            ↓
 Contradiction Signal
            ↓
      Support Score
            ↓
Supported / Review / Potentially Contradictory
```

Support score:

```text
0.55 × similarity + 0.45 × lexical_overlap − 0.35 × contradiction_signal
```

The score is clipped to 0–1.

## Dataset

15 synthetic examples covering literature, geography, history, science, mathematics, art, biology, research, economics, technology and data quality.

The dataset is synthetic and does not represent any real AI model's performance.

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Windows activation:

```powershell
.venv\\Scripts\\activate
```

## Run

```bash
python -m src.run_pipeline
```

Results are saved to `data/processed/factuality_results.csv` and `reports/factuality_report.md`.

For the interactive application:

```bash
streamlit run app/app.py
```

## Limitations

Lexical similarity cannot establish factual truth. Correct paraphrases can score lower, and incorrect answers can share many words with a reference. Numeric mismatch is only a heuristic. The reference answer can also be incomplete or wrong. The system does not independently retrieve or verify external evidence.

For high-stakes factuality assessment, claims should be checked against appropriate trusted sources and reviewed by humans.

## Future Improvements

- Semantic embeddings
- Claim-level extraction
- Retrieval from trusted sources
- Citation verification
- Precision/recall benchmarking
- Human annotation and adjudication
- Inter-rater reliability
- Comparison of multiple LLM judges

## Portfolio Skills

AI evaluation • hallucination analysis • factuality assessment • error analysis • Python • Pandas • Streamlit • testing • evaluation methodology

## Project Structure

```text
ai-hallucination-factuality-evaluator/
├── app/
├── data/
│   ├── raw/
│   └── processed/
├── src/
├── tests/
├── reports/
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

## License

MIT
