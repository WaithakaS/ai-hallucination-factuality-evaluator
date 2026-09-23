from difflib import SequenceMatcher
from .text_normalization import normalize, tokens

def lexical_overlap(reference, answer):
    ref, ans = set(tokens(reference)), set(tokens(answer))
    return 0.0 if not ans else len(ref & ans) / len(ans)

def similarity(reference, answer):
    return SequenceMatcher(None, normalize(reference), normalize(answer)).ratio()

def contradiction_signal(reference, answer):
    ref_numbers = {t for t in tokens(reference) if any(c.isdigit() for c in t)}
    ans_numbers = {t for t in tokens(answer) if any(c.isdigit() for c in t)}
    return 1.0 if ref_numbers and ans_numbers and ref_numbers.isdisjoint(ans_numbers) else 0.0

def evaluate_pair(reference, answer):
    sim = similarity(reference, answer)
    overlap = lexical_overlap(reference, answer)
    contradiction = contradiction_signal(reference, answer)
    score = max(0.0, min(1.0, 0.55*sim + 0.45*overlap - 0.35*contradiction))
    if contradiction:
        label = "potentially_unsupported_or_contradictory"
    elif score >= 0.75:
        label = "supported"
    elif score >= 0.45:
        label = "needs_review"
    else:
        label = "low_support"
    return {"similarity":round(sim,4),"lexical_overlap":round(overlap,4),"contradiction_signal":contradiction,"support_score":round(score,4),"label":label}

def evaluate_dataset(df):
    return [evaluate_pair(r.reference_answer, r.model_answer) for r in df.itertuples()]
