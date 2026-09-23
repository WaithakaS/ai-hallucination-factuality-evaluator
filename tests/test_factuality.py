from src.factuality import evaluate_pair, lexical_overlap

def test_identical_text_is_supported():
    r=evaluate_pair("Paris is the capital of France.","Paris is the capital of France.")
    assert r["support_score"] > .9
    assert r["label"]=="supported"

def test_numeric_contradiction():
    r=evaluate_pair("The Moon landing occurred in 1969.","The Moon landing occurred in 1972.")
    assert r["contradiction_signal"]==1.0

def test_empty_overlap():
    assert lexical_overlap("Paris is the capital.","")==0.0
