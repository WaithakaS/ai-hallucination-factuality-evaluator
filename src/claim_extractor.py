import re

def split_into_claims(text: str):
    return [p.strip() for p in re.split(r"(?<=[.!?])\s+", str(text).strip()) if p.strip()]
