RISK_WEIGHTS = {
    "urgency": 15,
    "threat": 25,
    "credential": 30,
    "financial": 20,
}

def calculate_score(indicators):
    score = 0

    for indicator in indicators:
        indicator_type = indicator["type"]
        score += RISK_WEIGHTS.get(indicator_type, 0)

    return min(score, 100)

def get_risk_level(score):
    if score >= 75:
        return "high"

    if score >= 40:
        return "medium"

    return "low
