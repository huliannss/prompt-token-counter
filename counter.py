def estimate_tokens(text: str) -> dict:
    words = len(text.split())
    tokens = int(words * 1.33) + 1
    return {'words': words, 'tokens': tokens, 'cost_usd': round(tokens * 0.00003, 6)}
