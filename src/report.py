from pathlib import Path
import pandas as pd

def generate_report(results_path, report_path):
    df = pd.read_csv(results_path)
    lines = [
        "# Factuality Evaluation Report", "",
        f"- Examples evaluated: {len(df)}",
        f"- Supported: {(df.label=='supported').sum()}",
        f"- Needs review: {(df.label=='needs_review').sum()}",
        f"- Potentially unsupported/contradictory: {(df.label=='potentially_unsupported_or_contradictory').sum()}",
        f"- Low support: {(df.label=='low_support').sum()}", "",
        f"- Mean similarity: {df.similarity.mean():.3f}",
        f"- Mean lexical overlap: {df.lexical_overlap.mean():.3f}",
        f"- Mean support score: {df.support_score.mean():.3f}", "",
        "## Important interpretation note", 
        "These are heuristic signals. A high similarity score does not prove truth, and a low score does not prove falsity. Human or source-based verification is required for high-stakes factuality assessment."
    ]
    Path(report_path).parent.mkdir(parents=True, exist_ok=True)
    Path(report_path).write_text("\n".join(lines), encoding="utf-8")
